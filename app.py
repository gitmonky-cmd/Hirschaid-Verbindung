import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. SEITENKONFIGURATION
st.set_page_config(
    page_title="Stau- & Kostenrechner Hirschaid-West",
    page_icon="🚗",
    layout="centered"
)

# 2. AKTUELLER AUFHÄNGER & MOTTO
st.warning("🚨 **AKTUELLE MELDUNG:** Vom 26.10. bis 26.11.2026 finden bereits Bohrarbeiten mit halbseitiger Sperrung auf der Kanalbrücke statt! Die Vorbereitungen für die Großsanierung laufen.")

st.title("Sagt hinterher nicht, keiner hätte gewusst, was auf uns zukommt!")
st.subheader("Brückensanierung ja, aber Wege in Hirschaid und nach Bamberg sichern, ohne Verkehrskollaps!")

st.markdown("""
*Die anstehenden Baustellen bedrohen die Verkehrsanbindung von Sassanfahrt, Erlach, Juliushof, 
Köttmannsdorf, Rothensand und Altendorf. Der Umweg über Frensdorf bedeutet massive Mehrkosten und Zeitverluste!*
""")

st.divider()

# 3. WARUM AKTIV WERDEN / DAS PROBLEM JETZT
st.header("⚠️ Warum aktiv werden? Das müssen Sie wissen:")

st.info("""
👉 **Wer plant hier eigentlich?**
* ❌ **Nicht Hirschaid entscheidet:** Weder der Bürgermeister noch der Gemeinderat haben hier die Planungsgewalt.
* 🏛️ **Das Staatliche Bauamt ist am Zug:** Die Landesbehörde muss die gealterten Brücken sanieren – blickt dabei aber oft nur auf die eigenen Baustellen.
* ✍️ **Ihre Unterschrift wirkt oben:** Nur über den **Bayerischen Landtag** können wir das Bauamt verpflichten, Koppelungsverbote und Behelfsbrücken verbindlich einzuplanen!
""")

# 4. WARUM JETZT ACTIEN? (DRINGLICHKEIT)
st.header("⏱️ Warum zählt JETZT jeder Tag?")

st.markdown("""
Mancher mag fragen: *„Die Hauptsanierung dauert doch noch – warum jetzt schon unterschreiben?“*  
Die Antwort ist einfach: **Weil die Weichen für die Verkehrsführung HEUTE gestellt werden!**

* 🚨 **Gefahr von unbemerkten Überschneidungen:** Wenn wir jetzt nicht aktiv werden, besteht die große Gefahr, dass sich die Sanierungs- und Bauarbeiten bei den verschiedenen Brücken (St 2244 & B 505) überschneiden.
* 🚨 **Handeln, bevor das Kind in den Brunnen fällt:** Erfahrungsgemäß erkennen Behörden die fatalen Überschneidungen erst, wenn die Verträge gezeichnet sind und die Vollsperrung steht – dann ist es für Alternativen zu spät.
* 🚨 **Langer Vorlauf für Behelfsbrücken:** Der Bau einer Behelfsbrücke im FFH-Naturschutzgebiet benötigt Monate an Umweltprüfungen und Genehmigungen. Wer erst bei Baubeginn danach ruft, steht jahrelang im Stau.
* 🚨 **Signale an die Entscheider senden:** Die Bohrarbeiten zeigen, dass die Detailplanungen laufen. Nur wenn wir **jetzt** eine starke Welle an Unterschriften vorlegen, zwingen wir das Bauamt dazu, Koppelungsverbote und Behelfsstrukturen von Anfang an fest einzuplanen!
""")

st.divider()

# 5. RECHNER (EINGABEFORMULAR)
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

# 6. ERGEBNISSE ANZEIGEN
st.header("📊 Deine Ergebnisse (Mehrbelastung bei Vollsperrung)")

k1, k2, k3 = st.columns(3)
k1.metric("Zusatz-Kilometer / Monat", f"{gesamte_zusatz_km_monat:.0f} km")
k2.metric("Sprit-Mehrkosten / Monat", f"{spritkosten_monat:.2f} €")
k3.metric("Zeitverlust / Jahr", f"{stunden_jahr:.0f} Std.")

st.warning(f"⚠️ **Hochrechnung für ein Baujahr:** Du fährst ca. **{gesamte_zusatz_km_jahr:.0f} km extra** und verbringst **{stunden_jahr:.0f} Stunden** zusätzlich im Auto!")

st.divider()

# 7. KARTEN-VISUALISIERUNG
st.header("🗺️ Die Umleitungsstrecke & Nadelöhre im Überblick")

# Kartenzentrum
m = folium.Map(location=[49.835, 10.915], zoom_start=11, tiles="OpenStreetMap")

# Marker 1: Sperrung Kanalbrücke St 2244
folium.Marker(
    location=[49.8168, 10.9835],
    popup="<b>SPERRUNG / SONDIERUNG:</b><br>Kanalbrücke St 2244 Hirschaid",
    tooltip="🚨 Nadelöhr 1: Kanalbrücke St 2244",
    icon=folium.Icon(color="red", icon="warning-sign")
).add_to(m)

# Marker 2: Sperrung/Engpass B 505
folium.Marker(
    location=[49.8250, 10.9480],
    popup="<b>BAUSTELLE / ENG PASS:</b><br>B 505 (Auffahrt / Brücken)",
    tooltip="🚨 Nadelöhr 2: B 505 / Anschlussstelle",
    icon=folium.Icon(color="orange", icon="warning-sign")
).add_to(m)

# Umleitungspunkte (Erlach -> Röbersdorf -> Herrnsdorf -> Frensdorf -> Bug -> Bamberg)
umleitung_punkte = [
    [49.8083, 10.9540],  # Erlach / Juliushof
    [49.7990, 10.9268],  # Röbersdorf
    [49.7942, 10.8852],  # Herrnsdorf
    [49.8159, 10.8661],  # Frensdorf
    [49.8674, 10.9052],  # Bug
    [49.8988, 10.9028]   # Bamberg Zentrum
]

# Umleitungs-Linie (Rot gestrichelt)
folium.PolyLine(
    locations=umleitung_punkte,
    color="red",
    weight=5,
    opacity=0.8,
    dash_array="10",
    tooltip="Ausweichroute für L6e & PKW (ca. 24,5 km)"
).add_to(m)

# Start / Ziel Marker
folium.Marker([49.8083, 10.9540], popup="Start: Hirschaid-West (Erlach/Juliushof)", icon=folium.Icon(color="green")).add_to(m)
folium.Marker([49.8988, 10.9028], popup="Ziel: Bamberg", icon=folium.Icon(color="blue")).add_to(m)

# Karte rendern
st_folium(m, width=700, height=450)

st.caption("🔴 **Rot gestrichelt:** Die unumgängliche Ausweichroute über Frensdorf & Bug bei Vollsperrung der Direktverbindungen.")

st.divider()

# 8. HANDLUNGSAUFFORDERUNG & UNTERSCHRIFTEN
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
    st.link_button("📲 WhatsApp-Community beitreten", "https://chat.whatsapp.com/KmCCa8tthhZ3SnvpuIuqfm")

with col_pet:
    st.link_button("✍️ Zur Online-Unterstützung", "https://www.openpetition.de/petition/online/brueckensanierung-ja-aber-wege-in-hirschaid-und-nach-bamberg-sichern-ohne-verkehrskollaps")

st.divider()

# 9. IMPRESSUM
# PLATZHALTER: **Herausgeber & Initiative:** Bürgerinitiative Hirschaid-Altendorf in Kooperation mit der Wählergemeinschaft West (WGW).
st.caption("""
**Kontakt / Verantwortlich:** Benjamin Bauer, Juliusring 2, 96114 Hirschaid
""")
