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

st.title("Sagt hinterher nicht, wir hätten es nicht gesagt!")
st.subheader("Brückensanierung ja, aber bitte nicht alle auf einmal!")

st.markdown("""
*Die anstehenden Baustellen bedrohen die Verkehrsanbindung von Sassanfahrt, Erlach, Juliushof, 
Köttmannsdorf, Rothensand und Altendorf. Der Umweg über Frensdorf bedeutet massive Mehrkosten und Zeitverluste!*
""")

st.divider()

# 3. WARUM AKTIV WERDEN / DAS PROBLEM JETZT
st.header("⚠️ Warum aktiv werden? Das müssen Sie wissen:")

st.info("""
👉 **Wer plant hier eigentlich, wann welche Brücke gesperrt wird?**
- ❌ **Nicht Hirschaid entscheidet:** Weder der Bürgermeister noch der Gemeinderat haben hier die Planungsgewalt.
- 🏛️ **Das Staatliche Bauamt ist am Zug:** Die Landesbehörde muss die gealterten Brücken sanieren – blickt dabei aber oft nur auf die eigenen Baustellen.
- ✍️ **Ihre Unterschrift wirkt oben:** Nur über den **Bayerischen Landtag** können wir das Bauamt verpflichten, Koppelungsverbote und Behelfsbrücken verbindlich einzuplanen!
""")

# 4. WARUM JETZT ACTIEN? (DRINGLICHKEIT)
st.header("⏱️ Warum zählt JETZT jeder Tag?")

st.markdown("""
Mancher mag fragen: *„Die Hauptsanierung dauert doch noch – warum jetzt schon unterschreiben?“*  
Die Antwort ist einfach: **Weil die Weichen für die Verkehrsführung HEUTE gestellt werden!**

- 🚨 **Gefahr von unbemerkten Überschneidungen:** Wenn wir jetzt nicht aktiv werden, besteht die große Gefahr, dass sich die Sanierungs- und Bauarbeiten bei den verschiedenen Brücken (St 2260 & B 505) überschneiden.

- 🚨 **Handeln, bevor das Kind in den Brunnen fällt:** Erfahrungsgemäß erkennen Behörden die fatalen Überschneidungen erst, wenn die Verträge gezeichnet sind und die Vollsperrung steht – dann ist es für Alternativen zu spät.

- 🚨 **Langer Vorlauf für Behelfsbrücken:** Der Bau einer Behelfsbrücke im FFH-Naturschutzgebiet benötigt Monate an Umweltprüfungen und Genehmigungen. Wer erst bei Baubeginn danach ruft, steht jahrelang im Stau.

- 🚨 **Signale an die Entscheider senden:** Die Bohrarbeiten zeigen, dass die Detailplanungen laufen. Nur wenn wir **jetzt** eine starke Welle an Unterschriften vorlegen, zwingen wir das Bauamt dazu, Koppelungsverbote und Behelfsstrukturen von Anfang an fest einzuplanen!
""")

st.divider()

# 5. RECHNER (EINGABEFORMULAR)
st.header("🧮 Berechne dein Stau- & Kostenrisiko")

col1, col2 = st.columns(2)

with col1:
    arbeitstage = st.slider("Fahrten pro Woche:", min_value=1, max_value=7, value=5)
    fahrzeug = st.selectbox("Fahrzeugtyp:", ["Standard-PKW", "Leichtkfz / L6e (45 km/h)"])

with col2:
    spritpreis = st.number_input("Spritpreis (€/Liter):", value=1.75, step=0.05)
    verbrauch = st.number_input("Verbrauch (L/100 km):", value=6.5, step=0.5)

st.divider()

# 6. SCENARIEN & RECHNER-ERGEBNISSE
st.header("📊 Szenarien-Vergleich & Betroffenheit")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Pendler Bamberg", 
    "Köttmannsdorf ➔ Zentrum", 
    "Juliushof ➔ Erlangen", 
    "Rothensand ➔ Realschule", 
    "Sassanfahrt ➔ Ärztehaus", 
    "Frensdorf ➔ Bahnhof"
])

# Hilfsfunktion für Berechnungen
def berechne_werte(umweg_km_einfach, zeit_min_einfach):
    zusatz_km_tag = umweg_km_einfach * 2
    zeitverlust_tag = (zeit_min_einfach * 2) if "PKW" in fahrzeug else (zeit_min_einfach * 1.5 * 2)
    tage_jahr = arbeitstage * 46
    
    km_monat = (zusatz_km_tag * arbeitstage * 52) / 12
    km_jahr = zusatz_km_tag * tage_jahr
    kosten_monat = (km_monat / 100) * verbrauch * spritpreis
    stunden_jahr = (zeitverlust_tag * tage_jahr) / 60
    return km_monat, kosten_monat, stunden_jahr, km_jahr

# --- TAB 1: Pendler Bamberg ---
with tab1:
    st.subheader("Pendlerstrecke: Hirschaid-West ➔ Bamberg")
    km_m, kost_m, std_j, km_j = berechne_werte(12.5, 15)
    
    k1, k2, k3 = st.columns(3)
    k1.metric("Zusatz-KM / Monat", f"{km_m:.0f} km")
    k2.metric("Mehrkosten / Monat", f"{kost_m:.2f} €")
    k3.metric("Zeitverlust / Jahr", f"{std_j:.0f} Std.")
    
    st.warning(f"⚠️ **Jahr hochgerechnet:** Ca. **{km_j:.0f} km Umweg** und **{std_j:.0f} Stunden** reine Umweg-Zeit pro Baujahr!")

    m1 = folium.Map(location=[49.835, 10.915], zoom_start=11)
    folium.PolyLine([[49.8083, 10.9540], [49.7990, 10.9268], [49.7942, 10.8852], [49.8159, 10.8661], [49.8674, 10.9052], [49.8988, 10.9028]], color="red", weight=5, dash_array="10").add_to(m1)
    folium.Marker([49.8083, 10.9540], popup="Start: Hirschaid-West", icon=folium.Icon(color="green")).add_to(m1)
    folium.Marker([49.8988, 10.9028], popup="Ziel: Bamberg", icon=folium.Icon(color="blue")).add_to(m1)
    st_folium(m1, width=700, height=350, key="map1")

# --- TAB 2: Köttmannsdorf ➔ Zentrum Hirschaid ---
with tab2:
    st.subheader("Köttmannsdorf ➔ Zentrum Hirschaid (Ohne Behelfsbrücke)")
    st.caption("Direktweg: ca. 2,5 km | Umweg über Strullendorf/B505 bzw. Frensdorf: ca. 14 km")
    km_m, kost_m, std_j, km_j = berechne_werte(11.5, 12)
    
    k1, k2, k3 = st.columns(3)
    k1.metric("Zusatz-KM / Monat", f"{km_m:.0f} km")
    k2.metric("Mehrkosten / Monat", f"{kost_m:.2f} €")
    k3.metric("Zeitverlust / Jahr", f"{std_j:.0f} Std.")
    
    st.warning(f"⚠️ **Der Wahnsinn hochgerechnet:** Ca. **{km_j:.0f} km Umweg** und **{std_j:.0f} Stunden** verlost für eine Strecke, die sonst nur 3 Minuten dauert!")

    m2 = folium.Map(location=[49.830, 10.950], zoom_start=12)
    folium.PolyLine([[49.8260, 10.9380], [49.8550, 10.9500], [49.8168, 10.9900]], color="red", weight=5, dash_array="10").add_to(m2)
    folium.Marker([49.8260, 10.9380], popup="Start: Köttmannsdorf", icon=folium.Icon(color="green")).add_to(m2)
    folium.Marker([49.8168, 10.9900], popup="Ziel: Zentrum Hirschaid", icon=folium.Icon(color="blue")).add_to(m2)
    st_folium(m2, width=700, height=350, key="map2")

# --- TAB 3: Juliushof ➔ Erlangen ---
with tab3:
    st.subheader("Juliushof ➔ Erlangen / Süden")
    st.caption("Auffahrt Hirschaid/B505 dicht: Ausweichen über Höchstadt/A3 oder Altendorf/Buttenheim")
    km_m, kost_m, std_j, km_j = berechne_werte(8.0, 10)
    
    k1, k2, k3 = st.columns(3)
    k1.metric("Zusatz-KM / Monat", f"{km_m:.0f} km")
    k2.metric("Mehrkosten / Monat", f"{kost_m:.2f} €")
    k3.metric("Zeitverlust / Jahr", f"{std_j:.0f} Std.")
    
    st.warning(f"⚠️ **Jahr hochgerechnet:** Ca. **{km_j:.0f} km Umweg** und **{std_j:.0f} Stunden** zusätzlicher Zeitverlust Richtung Süden!")

    m3 = folium.Map(location=[49.750, 10.950], zoom_start=11)
    folium.PolyLine([[49.8020, 10.9480], [49.7900, 10.9800], [49.7700, 10.9900], [49.5960, 11.0040]], color="red", weight=5, dash_array="10").add_to(m3)
    folium.Marker([49.8020, 10.9480], popup="Start: Juliushof", icon=folium.Icon(color="green")).add_to(m3)
    folium.Marker([49.5960, 11.0040], popup="Ziel: Erlangen", icon=folium.Icon(color="blue")).add_to(m3)
    st_folium(m3, width=700, height=350, key="map3")

# --- TAB 4: Rothensand ➔ Realschule Hirschaid ---
with tab4:
    st.subheader("Rothensand ➔ Realschule Hirschaid (Schulweg)")
    st.caption("Kein Schulbus durch die Sperrung: Umleitung der Busse über Seußling/Altendorf")
    km_m, kost_m, std_j, km_j = berechne_werte(7.5, 12)
    
    k1, k2, k3 = st.columns(3)
    k1.metric("Zusatz-KM / Monat", f"{km_m:.0f} km")
    k2.metric("Mehrkosten / Monat", f"{kost_m:.2f} €")
    k3.metric("Zeitverlust / Jahr", f"{std_j:.0f} Std.")
    
    st.warning(f"⚠️ **Schulweg-Belastung hochgerechnet:** Ca. **{km_j:.0f} km Umweg** und **{std_j:.0f} Stunden** Zeitverlust für Schüler und Elterntaxis!")

    m4 = folium.Map(location=[49.800, 10.950], zoom_start=12)
    folium.PolyLine([[49.7820, 10.9320], [49.7750, 10.9650], [49.8130, 10.9920]], color="red", weight=5, dash_array="10").add_to(m4)
    folium.Marker([49.7820, 10.9320], popup="Start: Rothensand", icon=folium.Icon(color="green")).add_to(m4)
    folium.Marker([49.8130, 10.9920], popup="Ziel: Realschule Hirschaid", icon=folium.Icon(color="blue")).add_to(m4)
    st_folium(m4, width=700, height=350, key="map4")

# --- TAB 5: Sassanfahrt ➔ Ärztehaus Hirschaid ---
with tab5:
    st.subheader("Sassanfahrt ➔ Ärztehaus / Apotheken Hirschaid")
    st.caption("Besonders kritisch für Senioren & Krankenfahrten ohne Behelfsbrücke!")
    km_m, kost_m, std_j, km_j = berechne_werte(9.0, 15)
    
    k1, k2, k3 = st.columns(3)
    k1.metric("Zusatz-KM / Monat", f"{km_m:.0f} km")
    k2.metric("Mehrkosten / Monat", f"{kost_m:.2f} €")
    k3.metric("Zeitverlust / Jahr", f"{std_j:.0f} Std.")
    
    st.warning(f"⚠️ **Gesundheitsversorgung hochgerechnet:** Ca. **{km_j:.0f} km Umweg** und **{std_j:.0f} Stunden** Mehraufwand für Patientenfahrten!")

    m5 = folium.Map(location=[49.815, 10.960], zoom_start=12)
    folium.PolyLine([[49.8120, 10.9480], [49.7900, 10.9600], [49.8180, 10.9880]], color="red", weight=5, dash_array="10").add_to(m5)
    folium.Marker([49.8120, 10.9480], popup="Start: Sassanfahrt", icon=folium.Icon(color="green")).add_to(m5)
    folium.Marker([49.8180, 10.9880], popup="Ziel: Ärztehaus Hirschaid", icon=folium.Icon(color="blue")).add_to(m5)
    st_folium(m5, width=700, height=350, key="map5")

# --- TAB 6: Frensdorf ➔ Bahnhof Hirschaid ---
with tab6:
    st.subheader("Frensdorf ➔ Bahnhof Hirschaid (P&R Pendler)")
    st.caption("Bahnhof Hirschaid nicht mehr direkt von Westen erreichbar")
    km_m, kost_m, std_j, km_j = berechne_werte(10.0, 14)
    
    k1, k2, k3 = st.columns(3)
    k1.metric("Zusatz-KM / Monat", f"{km_m:.0f} km")
    k2.metric("Mehrkosten / Monat", f"{kost_m:.2f} €")
    k3.metric("Zeitverlust / Jahr", f"{std_j:.0f} Std.")
    
    st.warning(f"⚠️ **P&R Pendler hochgerechnet:** Ca. **{km_j:.0f} km Umweg** und **{std_j:.0f} Stunden** Lebenszeit im Stau vor dem Zug!")

    m6 = folium.Map(location=[49.820, 10.920], zoom_start=12)
    folium.PolyLine([[49.8159, 10.8661], [49.7942, 10.8852], [49.7750, 10.9650], [49.8170, 10.9880]], color="red", weight=5, dash_array="10").add_to(m6)
    folium.Marker([49.8159, 10.8661], popup="Start: Frensdorf", icon=folium.Icon(color="green")).add_to(m6)
    folium.Marker([49.8170, 10.9880], popup="Ziel: Bahnhof Hirschaid", icon=folium.Icon(color="blue")).add_to(m6)
    st_folium(m6, width=700, height=350, key="map6")

st.divider()

# 7. HANDLUNGSAUFFORDERUNG & UNTERSCHRIFTEN
st.header("🛑 Damit nicht beide Brücken gleichzeitig gesperrt werden (B 505 & Kanalbrücke Hirschaid (St 2260)!")
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

# 8. IMPRESSUM
# PLATZHALTER: **Herausgeber & Initiative:** Bürgerinitiative Hirschaid-Altendorf in Kooperation mit der Wählergemeinschaft West (WGW).
st.caption("""
**Kontakt / Verantwortlich:** Benjamin Bauer, Juliusring 2, 96114 Hirschaid
""")
