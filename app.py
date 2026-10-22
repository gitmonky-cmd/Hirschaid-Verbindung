import streamlit as st

# Seitenkonfiguration
st.set_page_config(
    page_title="Stau- & Kostenrechner Hirschaid-West",
    page_icon="🚗",
    layout="centered"
)

# Aktueller Aufhänger
st.warning("🚨 **AKTUELLE MELDUNG:** Vom 26.10. bis 26.11.2026 finden bereits Bohrarbeiten mit halbseitiger Sperrung auf der Kanalbrücke statt! Die Vorbereitungen für die Großsanierung laufen.")

# Titel & Wachrüttler-Motto
st.title("Sagt hinterher nicht, keiner hätte gewusst, was auf uns zukommt!")
st.subheader("Wenn Kanalbrücke & B 505 gleichzeitig saniert werden, steht der Hirschaider Westen still.")

st.markdown("""
*Die anstehenden Baustellen bedrohen die Verkehrsanbindung von Sasanfahrt, Erlach, Juliushof, 
Köttmannsdorf, Rothensand und Altendorf. Der Umweg über Frensdorf bedeutet massive Mehrkosten und Zeitverluste!*
""")

st.divider()

# Eingabeformular
st.header("🧮 Berechne dein Stau- & Kostenrisiko")

col1, col2 = st.columns(2)

with col1:
    arbeitstage = st.slider("Arbeitstage pro Woche nach Bamberg:", min_value=1, max_value=7, value=5)
    fahrzeug = st.selectbox("Fahrzeugtyp:", ["Standard-PKW", "Leichtkfz / L6e (45 km/h)"])

with col2:
    spritpreis = st.number_input("Spritpreis (€/Liter):", value=1.75, step=0.05)
    verbrauch = st.number_input("Verbrauch (L/100 km):", value=6.5, step=0.5)

# Berechnungskonstanten
umweg_pro_strecke = 24.5 - 12.0  # 12.5 km Mehrweg pro Fahrt
zusatz_km_tag = umweg_pro_strecke * 2

zeitverlust_fahrt = 15 if "PKW" in fahrzeug else 25
zeitverlust_tag = zeitverlust_fahrt * 2

wochen_pro_jahr = 46
tage_jahr = arbeitstage * wochen_pro_jahr

gesamte_zusatz_km_monat = (zusatz_km_tag * arbeitstage * 52) / 12
gesamte_zusatz_km_jahr = zusatz_km_tag * tage_jahr

spritkosten_monat = (gesamte_zusatz_km_monat / 100) * verbrauch * spritpreis
stunden_jahr = (zeitverlust_tag * tage_jahr) / 60

st.divider()

# Ergebnisse anzeigen
st.header("📊 Deine Ergebnisse (Mehrbelastung bei Vollsperrung)")

k1, k2, k3 = st.columns(3)
k1.metric("Zusatz-Kilometer / Monat", f"{gesamte_zusatz_km_monat:.0f} km")
k2.metric("Sprit-Mehrkosten / Monat", f"{spritkosten_monat:.2f} €")
k3.metric("Zeitverlust / Jahr", f"{stunden_jahr:.0f} Std.")

st.warning(f"⚠️ **Hochrechnung für ein Baujahr:** Du fährst ca. **{gesamte_zusatz_km_jahr:.0f} km extra** und verbringst **{stunden_jahr:.0f} Stunden** zusätzlich im Auto!")

st.divider()

# Handlungsaufforderung & Unterschriften-Hinweis
st.header("✍️ Jetzt handeln – Rechtswirksam unterschreiben!")

st.error("""
**WICHTIGER HINWEIS ZUR RECHTSSICHERHEIT:**  
Reine Online-Klicks reichen für die Übergabe an den Bayerischen Landtag oft nicht aus. 
**Nur händisch geleistete Unterschriften auf der Papierliste sind rechtlich zu 100 % wirksam!**
""")

st.markdown("""
### So verpasst du keinen Auslegeort:
1. **Tritt der WhatsApp-Community bei:** Dort erfährst du sofort, wo in den Ortsteilen (Bäckereien, Geschäfte, Infostände) die offiziellen Unterschriftenlisten ausliegen.
2. Trage dich unten zur digitalen Unterstützung ein, um den Fortschritt zu verfolgen.
""")

col_wa, col_pet = st.columns(2)

with col_wa:
    st.link_button("📲 WhatsApp-Community beitreten", "https://chat.whatsapp.com/DEIN_LINK_HIER")

with col_pet:
    st.link_button("✍️ Zur Online-Unterstützung", "https://DEINE_ONLINE_PETITION_URL")

st.divider()

# Impressum / Legal Section
st.caption("""
**Herausgeber & Initiative:** Bürgerinitiative Hirschaid-West / Altendorf in Kooperation mit der Wählergemeinschaft West (WGW).  
**Kontakt / Verantwortlich:** [Dein Name/Vertreter], [Straße, Hausnummer], [PLZ Ort], E-Mail: [Deine E-Mail]
""")
