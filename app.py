# app.py
# EcoSwitch Landing – Streamlit (Starlink-like / Minimal)
# - Dark/Light toggle
# - Data-driven content (steps, FAQ)
# - ASCII-safe (no curly quotes)
# - Replace image URLs with your own assets as needed

import streamlit as st

# ---------- Page setup ----------
st.set_page_config(
    page_title="EcoSwitch – Engineered for Truth",
    page_icon="⚡",
    layout="wide",
)

# ---------- Theme state ----------
if "is_dark" not in st.session_state:
    st.session_state.is_dark = True

def toggle_theme():
    st.session_state.is_dark = not st.session_state.is_dark

# CSS variables for both themes
DARK_VARS = {
    "--bg": "#0B0F14",
    "--fg": "#FFFFFF",
    "--muted": "rgba(255,255,255,0.70)",
    "--card": "rgba(255,255,255,0.05)",
    "--cardHover": "rgba(255,255,255,0.10)",
    "--ring": "rgba(255,255,255,0.12)",
    "--accent": "#8CF0C7",
}
LIGHT_VARS = {
    "--bg": "#F7F9FB",
    "--fg": "#0B0F14",
    "--muted": "#2B2F36",
    "--card": "#FFFFFF",
    "--cardHover": "#F1F5F9",
    "--ring": "rgba(0,0,0,0.08)",
    "--accent": "#00A878",
}
vars_used = DARK_VARS if st.session_state.is_dark else LIGHT_VARS

# ---------- Global styles ----------
st.markdown(
    f"""
    <style>
      :root {{
        {"".join([f"{k}:{v};" for k,v in vars_used.items()])}
      }}
      html, body, [data-testid="stAppViewContainer"] {{
        background: var(--bg) !important;
        color: var(--fg) !important;
      }}
      .hero-gradient {{
        background: radial-gradient(80% 50% at 50% -10%, color-mix(in oklab, var(--accent) 20%, transparent), transparent 60%);
      }}
      .muted {{ color: var(--muted); }}
      .card {{
        background: var(--card);
        border: 1px solid var(--ring);
        border-radius: 16px;
        padding: 20px;
      }}
      .badge {{
        display:inline-flex; align-items:center; gap:.5rem;
        padding:.35rem .75rem; border-radius:9999px;
        border:1px solid var(--ring); color: var(--muted);
        transition: transform .15s ease;
      }}
      .badge:hover {{ transform: scale(1.02); }}
      .cta {{
        display:inline-flex; align-items:center; justify-content:center; gap:.5rem;
        padding:.8rem 1.25rem; border-radius:16px; font-weight:600; text-decoration:none;
        border:1px solid transparent;
      }}
      .cta-primary {{ background: var(--fg); color: var(--bg); }}
      .cta-primary:hover {{ filter: brightness(0.95); }}
      .cta-secondary {{ background: var(--bg); color: var(--fg); border-color: var(--ring); }}
      .cta-secondary:hover {{ filter: brightness(1.05); }}
      .icon-circle {{
        width:40px; height:40px; border-radius:9999px;
        background: var(--card); border:1px solid var(--ring);
        display:flex; align-items:center; justify-content:center;
      }}
      .ring {{ border:1px solid var(--ring); border-radius:24px; }}
      .footer-cta {{ background: var(--cardHover); padding: 48px 24px; border-top:1px solid var(--ring); }}
      .accent {{ color: var(--accent); }}
      .img {{
        width:100%; height: auto; border-radius:24px; border:1px solid var(--ring);
      }}
      .center {{ text-align:center; }}
      .h1 {{ font-weight:700; font-size:clamp(32px,5vw,56px); letter-spacing:-0.02em; }}
      .h2 {{ font-weight:700; font-size:clamp(24px,3vw,34px); letter-spacing:-0.01em; }}
      .lead {{ font-size:18px; line-height:1.5; }}
      .grid-3 {{
        display:grid; gap:16px;
        grid-template-columns: 1fr;
      }}
      @media (min-width: 900px) {{
        .grid-3 {{ grid-template-columns: repeat(3, 1fr); }}
      }}
      .grid-2 {{
        display:grid; gap:24px;
        grid-template-columns: 1fr;
        align-items:center;
      }}
      @media (min-width: 992px) {{
        .grid-2 {{ grid-template-columns: 1.05fr 1fr; }}
      }}
      /* hide Streamlit default header/footer */
      header [data-testid="stToolbar"] {{ display:none !important; }}
      footer {{ visibility:hidden; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Content sources (data-driven) ----------
steps = [
    {
        "icon": "✅",
        "title": "1. Installer",
        "text": "Connectez EcoSwitch a votre systeme de chauffage. Installation simple, design discret.",
    },
    {
        "icon": "🖥️",
        "title": "2. Mesurer",
        "text": "L appareil observe et analyse vos cycles de consommation reels, 24/7. Une mesure precise, sans interruption.",
    },
    {
        "icon": "⚖️",
        "title": "3. Decider",
        "text": "Recevez un rapport factuel. Trois scenarios compares systematiquement: PAC, hybride, statu quo.",
    },
]

faq = [
    {
        "q": "Est-ce un outil pro-PAC ?",
        "a": "Non. EcoSwitch compare systematiquement trois scenarios – PAC, hybride, statu quo – avec des donnees objectives basees sur votre maison. Notre algorithme est concu pour reveler, pas pour orienter.",
    },
    {
        "q": "Comment mes donnees sont-elles protegees ?",
        "a": "EcoSwitch traite vos donnees localement, sans stockage cloud ni partage avec des tiers. Votre maison, vos donnees, vos preuves.",
    },
    {
        "q": "Ai-je besoin d un installateur ?",
        "a": "Non, EcoSwitch est concu pour etre intuitif. Mais nos partenaires peuvent vous accompagner si vous le souhaitez.",
    },
    {
        "q": "L audit peut-il etre offert ?",
        "a": "Oui. C est une pratique courante chez nos partenaires. Le cout du diagnostic EcoSwitch (199 € TTC) peut etre integre ou deduit si vous engagez les travaux avec un installateur partenaire.",
    },
]

# Placeholder images (remplace par tes assets locaux ou URLs)
IMG_PRODUCT = "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?q=80&w=1600&auto=format&fit=crop"  # visuel produit minimal
IMG_CUTAWAY = "https://images.unsplash.com/photo-1518779578993-ec3579fee39f?q=80&w=1600&auto=format&fit=crop"  # schema local compute
IMG_HANDSHAKE = "https://images.unsplash.com/photo-1523958203904-cdcb402031fd?q=80&w=1600&auto=format&fit=crop"  # relation pro

# ---------- Theme toggle ----------
col_toggle = st.columns([1,1,1,1,1,1,1,1,1,1,1,1])
with col_toggle[-1]:
    label = "Activate light mode" if st.session_state.is_dark else "Activate dark mode"
    if st.button(("☀️ Light" if st.session_state.is_dark else "🌙 Dark"), help=label):
        toggle_theme()

# ---------- HERO ----------
st.markdown(
    """
    <section class="hero-gradient" style="padding: 64px 0 72px;">
      <div class="center">
        <p class="muted" style="text-transform:uppercase; letter-spacing:.3em; font-size:12px;">EcoSwitch – Engineered for Truth</p>
        <h1 class="h1" style="margin-top:8px;">Votre maison, vos donnees, vos preuves.</h1>
        <p class="lead muted" style="max-width:860px; margin:16px auto 0;">
          Mesurez, comparez, decidez. EcoSwitch analyse trois scenarios – PAC, hybride, statu quo – avec une precision scientifique. Sans biais, sans compromis.
        </p>
        <div style="margin-top:18px;">
          <span class="badge"><span class="accent">●</span> Neutralite Certifiee – Donnees Protegees</span>
        </div>
        <div style="margin-top:28px;">
          <a href="#commande" class="cta cta-primary">Commander votre diagnostic</a>
          <span style="display:inline-block; width:10px;"></span>
          <a href="#methode" class="cta cta-secondary">Decouvrir la methode</a>
        </div>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# ---------- STEPS ----------
st.markdown(
    """
    <section style="padding: 8px 0;">
      <h2 class="h2">La clarte en trois etapes</h2>
      <p class="muted">Votre maison, vos donnees, vos preuves.</p>
    </section>
    """,
    unsafe_allow_html=True,
)
st.markdown('<div class="grid-3" style="margin-top:16px;">', unsafe_allow_html=True)
for s in steps:
    st.markdown(
        f"""
        <div class="card" style="transition: transform .15s ease;">
          <div class="icon-circle" aria-hidden="true">{s['icon']}</div>
          <h3 style="margin-top:10px; font-weight:700; font-size:18px;">{s['title']}</h3>
          <p class="muted" style="margin-top:6px; font-size:15px; line-height:1.6;">{s['text']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)

# ---------- NEUTRALITE ABSOLUE ----------
left, right = st.columns([1.05, 1])
with left:
    st.markdown(
        """
        <section style="padding-top:36px;">
          <h2 class="h2" id="neutralite">Neutralite Absolue</h2>
          <p class="lead muted" id="neutralite-desc" style="margin-top:12px;">
            EcoSwitch ne conseille pas. Il revele la verite energetique de votre maison.
            Chaque analyse compare trois scenarios – pompe a chaleur, systeme hybride, statu quo – avec des donnees objectives.
            Votre maison, vos donnees, vos preuves.
          </p>
        </section>
        """,
        unsafe_allow_html=True,
    )
with right:
    st.image(IMG_PRODUCT, use_column_width=True, caption=None)

# ---------- INTELLIGENCE LOCALE ----------
l2, r2 = st.columns([1, 1.05])
with l2:
    st.image(IMG_CUTAWAY, use_column_width=True, caption=None)
with r2:
    st.markdown(
        """
        <section id="methode" style="padding-top:36px;">
          <h2 class="h2">Intelligence Locale</h2>
          <p class="lead muted" id="locale-desc" style="margin-top:12px;">
            Vos donnees restent chez vous. EcoSwitch traite tout en local, sans cloud ni partage.
            Un algorithme concu pour la precision, pas pour la collecte. Votre maison, vos donnees, vos preuves.
          </p>
        </section>
        """,
        unsafe_allow_html=True,
    )

# ---------- PROS ----------
pL, pR = st.columns([1.05, 1])
with pL:
    st.markdown(
        """
        <section style="padding-top:36px;">
          <h2 class="h2" id="pros">EcoSwitch, plebiscite par les pros</h2>
          <p class="lead muted" style="margin-top:12px;">
            Des centaines d installateurs partenaires utilisent EcoSwitch pour garantir des recommandations fiables et transparentes,
            reduisant les litiges et augmentant la satisfaction client. Rejoignez un reseau qui mise sur la preuve.
          </p>
          <div style="margin-top:16px;">
            <a href="#partenaire" class="cta cta-primary">Devenir partenaire EcoSwitch</a>
            <span style="display:inline-block; width:10px;"></span>
            <a href="#installateur" class="cta cta-secondary">Trouver un installateur</a>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
with pR:
    st.image(IMG_HANDSHAKE, use_column_width=True, caption=None)

# ---------- DISTRIBUTEURS ----------
dL, dR = st.columns([1, 1.05])
with dL:
    st.image(IMG_PRODUCT, use_column_width=True, caption=None)
with dR:
    st.markdown(
        """
        <section style="padding-top:36px;">
          <h2 class="h2" id="distributeurs">EcoSwitch pour distributeurs: Boostez vos ventes avec la preuve</h2>
          <ul class="muted" style="margin-top:10px; line-height:1.7;">
            <li>Chaque EcoSwitch pose cree un pipeline de travaux chauffage</li>
            <li>Formations commerciales et co-branding disponibles</li>
            <li>Packs chantier: PAC + EcoSwitch, logistique simplifiee</li>
          </ul>
          <div style="margin-top:16px;">
            <a href="#distrib" class="cta cta-primary">Devenir distributeur partenaire</a>
            <span style="display:inline-block; width:10px;"></span>
            <a href="#kit-distrib" class="cta cta-secondary">Telecharger le kit distributeur</a>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

# ---------- FAQ ----------
st.markdown(
    """
    <section style="padding-top:36px; max-width:900px;">
      <h2 class="h2" id="faq">Questions frequentes</h2>
    </section>
    """,
    unsafe_allow_html=True,
)
for item in faq:
    with st.expander(item["q"], expanded=False):
        st.markdown(f"<p class='muted' style='margin:0'>{item['a']}</p>", unsafe_allow_html=True)

# ---------- FOOTER CTA ----------
st.markdown(
    """
    <section id="commande" class="footer-cta center">
      <h2 class="h2" style="margin-bottom:8px;">Pret a reveler la verite energetique de votre maison ?</h2>
      <p class="muted">Votre maison, vos donnees, vos preuves.</p>
      <div style="margin-top:18px;">
        <a href="#" class="cta cta-primary">Commander votre EcoSwitch</a>
      </div>
      <div class="muted" style="margin-top:10px; font-size:14px;">
        EcoSwitch - Engineered for Truth. | Mentions Legales | White Paper Scientifique | Espace Pro
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)
