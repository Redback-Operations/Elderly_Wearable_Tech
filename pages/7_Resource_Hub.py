# 7_Resource_Hub.py
import io
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Resource Hub / Local Services Finder", layout="wide")

st.title("📍 Resource Hub / Local Services Finder")
st.caption("Find nearby health and activity supports for families and caregivers. Data stays local to this session.")

# --- Expected schema ---
REQUIRED_COLS = [
    "name","type","tags","address","suburb","postcode","state",
    "lat","lon","phone","website","hours","cost","eligibility"
]

with st.expander("Expected columns (in any order)", expanded=False):
    st.code(", ".join(REQUIRED_COLS))

# ---------- Robust CSV loader ----------
def load_services_df(uploaded_file: bytes | None) -> pd.DataFrame:
    """Read user CSV safely. Auto-detect delimiter, handle encodings, validate columns."""
    if not uploaded_file:
        return pd.DataFrame(columns=REQUIRED_COLS)

    raw = uploaded_file.read() if hasattr(uploaded_file, "read") else uploaded_file
    attempts = []

    # 1) Try pandas sniffing with different encodings/engines
    for enc in ("utf-8", "utf-8-sig", "cp1252"):
        for engine in ("python", "c"):
            try:
                buf = io.BytesIO(raw)
                df = pd.read_csv(
                    buf,
                    sep=None,            # auto-detect , ; | \t
                    engine=engine,
                    encoding=enc,   
                    dtype=str,
                    on_bad_lines="skip"  # skip malformed rows instead of raising
                )
                df.columns = [c.strip().lower() for c in df.columns]

                # Check columns
                missing = [c for c in REQUIRED_COLS if c not in df.columns]
                if missing:
                    raise ValueError(f"Missing columns: {missing}")

                # Types and cleaning
                for c in ("lat", "lon"):
                    df[c] = pd.to_numeric(df[c], errors="coerce")
                df["postcode"] = df["postcode"].astype(str).str.replace(r"\.0$", "", regex=True)
                # Reorder/select
                return df[REQUIRED_COLS]
            except Exception as e:
                attempts.append(f"{enc}/{engine}: {type(e).__name__}: {e}")

    # 2) Fallback: explicit regex of common separators
    try:
        buf = io.BytesIO(raw)
        df = pd.read_csv(
            buf, sep=r"[,\t|;]", engine="python", encoding="utf-8", dtype=str, on_bad_lines="skip"
        )
        df.columns = [c.strip().lower() for c in df.columns]
        missing = [c for c in REQUIRED_COLS if c not in df.columns]
        if missing:
            raise ValueError(f"Missing columns after fallback: {missing}")
        for c in ("lat", "lon"):
            df[c] = pd.to_numeric(df[c], errors="coerce")
        df["postcode"] = df["postcode"].astype(str).str.replace(r"\.0$", "", regex=True)
        return df[REQUIRED_COLS]
    except Exception as e:
        attempts.append(f"fallback: {type(e).__name__}: {e}")

    st.error("Could not read CSV. Please check the header and delimiters.")
    st.caption("Attempts → " + " | ".join(attempts))
    return pd.DataFrame(columns=REQUIRED_COLS)

# ---------- Demo data toggle ----------
demo_rows = [
    ["Burwood Community Health Centre","GP Clinic","bulk-billing,family","2 Warrigal Rd","Burwood","3125","VIC",-37.8497,145.1127,"(03) 9800 1111","https://www.burwoodhealth.org","Mon–Fri 8–6; Sat 9–1","Bulk-billing available","All ages; Medicare card"],
    ["Deakin University Health & Wellbeing","Nutrition Workshop","students,free,workshop","221 Burwood Hwy","Burwood","3125","VIC",-37.847,145.114,"(03) 9244 6100","https://www.deakin.edu.au","Mon–Fri 9–5","Free for students","Students & staff"],
    ["Burwood Neighbourhood House","Activity Program","kids,after-school,community","1 Church St","Burwood","3125","VIC",-37.852,145.099,"(03) 9808 6292","https://www.burwoodneighbourhoodhouse.org.au","Mon–Fri 9–6","Low-cost","Children & families"],
    ["Eastern Mental Health Service","Mental Health","counselling,youth,adults","34 Station St","Burwood","3125","VIC",-37.854,145.105,"(03) 9887 1234","https://www.easternhealth.org.au","24/7","Free","All residents"],
    ["Whitehorse Council Recreation Centre","Council Recreation","sports,swimming,fitness","42 Burwood Hwy","Burwood","3125","VIC",-37.85,145.12,"(03) 9262 6333","https://www.whitehorse.vic.gov.au","Mon–Sun 6–9","Membership fees","Open to all"],
]

demo_df = pd.DataFrame(demo_rows, columns=REQUIRED_COLS)

col_left, col_right = st.columns([1,1])
with col_left:
    uploaded = st.file_uploader("Upload services file (CSV)", type=["csv"])
with col_right:
    use_demo = st.toggle("Use built-in Burwood demo data", value=(uploaded is None))

if uploaded and not use_demo:
    df = load_services_df(uploaded)
else:
    df = demo_df.copy()

# ---------- Filters ----------
st.subheader("🔎 Search & Filters")
c1, c2, c3, c4 = st.columns([1,1,1,1])

with c1:
    suburb = st.selectbox("Suburb", ["(All)"] + sorted(df["suburb"].dropna().unique().tolist()))
with c2:
    types = st.multiselect("Type", sorted(df["type"].dropna().unique().tolist()))
with c3:
    tag_query = st.text_input("Tags contains (comma-separated)", placeholder="free, kids, evening")
with c4:
    only_free = st.checkbox("Show free/low-cost")

filtered = df.copy()
if suburb and suburb != "(All)":
    filtered = filtered[filtered["suburb"].str.lower() == suburb.lower()]
if types:
    filtered = filtered[filtered["type"].isin(types)]
if tag_query.strip():
    terms = [t.strip().lower() for t in tag_query.split(",") if t.strip()]
    filtered = filtered[filtered["tags"].str.lower().fillna("").apply(lambda x: any(t in x for t in terms))]
if only_free:
    filtered = filtered[filtered["cost"].str.lower().str.contains("free|low", na=False)]

st.write(f"**Results:** {len(filtered)} services")
st.dataframe(filtered, use_container_width=True, hide_index=True)

# ---------- Map ----------
st.subheader("🗺️ Map")
map_df = filtered.dropna(subset=["lat","lon"])[["lat","lon","name","type","suburb"]]
if not map_df.empty:
    st.map(map_df, latitude="lat", longitude="lon", size=80, color="#22c55e")
else:
    st.info("No mappable rows (missing lat/lon).")

# ---------- Download filtered data ----------
st.download_button(
    "Download filtered CSV",
    data=filtered.to_csv(index=False).encode("utf-8"),
    file_name="services_filtered.csv",
    mime="text/csv"
)
