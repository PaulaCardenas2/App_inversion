import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="App Educativa de Inversiones 💰", layout="wide")

st.title("App Educativa de Inversiones y Pensiones 💰🏡✈️")
st.markdown("""
Bienvenido/a a la app interactiva para aprender sobre **inversiones y ahorro pensional**.  
Aquí podrás simular cómo tu dinero puede crecer con el tiempo y alcanzar tus metas.
""")

# -----------------------------
# Sidebar inputs
# -----------------------------
st.sidebar.header("Tus datos")
ahorro_mensual = st.sidebar.number_input("Ahorro mensual ($)", min_value=0, value=500000, step=10000)
años = st.sidebar.number_input("Años de ahorro", min_value=1, max_value=50, value=10)
edad = st.sidebar.number_input("Tu edad", min_value=18, max_value=70, value=25)
objetivo = st.sidebar.selectbox("Objetivo financiero", ["Fondo de pensión 🏦", "CDT 💵", "Finca raíz / apartamento 🏡", "Viaje ✈️"])

# -----------------------------
# Tabs
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs(["💰 Simulación", "📈 Comparador", "👨‍🏫 Educación", "📝 Consejos"])

# -----------------------------
# Tab 1: Simulación de ahorro
# -----------------------------
with tab1:
    st.subheader("📊 Simulación de tu ahorro")
    interes_anual = 0.05  # 5% anual
    meses = años * 12
    saldo = []
    capital = 0
    for i in range(1, meses+1):
        capital = capital + ahorro_mensual
        capital = capital * (1 + interes_anual/12)
        saldo.append(capital)
    
    st.line_chart(saldo)

    st.subheader("💡 Resumen")
    st.markdown(f"""
- Objetivo: **{objetivo}**
- Ahorro mensual: ${ahorro_mensual:,.0f}
- Tiempo: {años} años
- Interés anual aplicado: {interes_anual*100:.1f}%
- Capital acumulado aproximado: ${saldo[-1]:,.0f}
""")

# -----------------------------
# Tab 2: Comparador de estrategias
# -----------------------------
with tab2:
    st.subheader("📈 Comparador de estrategias de inversión")
    estrategias = {
        "CDT 💵": 0.04,
        "Fondo pensión 🏦": 0.05,
        "Finca raíz / apartamento 🏡": 0.06
    }
    comparacion = {}
    for clave, tasa in estrategias.items():
        saldo_temp = 0
        saldo_list = []
        for i in range(1, meses+1):
            saldo_temp += ahorro_mensual
            saldo_temp *= (1 + tasa/12)
            saldo_list.append(saldo_temp)
        comparacion[clave] = saldo_list
    df_comp = pd.DataFrame(comparacion)
    st.line_chart(df_comp)
    st.markdown("Puedes comparar cuánto crecería tu dinero según la estrategia elegida.")

# -----------------------------
# Tab 3: Educación financiera
# -----------------------------
with tab3:
    st.subheader("👨‍🏫 Educación financiera")
    st.markdown("""
- **Pensiones:** Ahorro obligatorio y voluntario para asegurar tu retiro.
- **Ahorro:** La constancia es clave, incluso montos pequeños crecen con el tiempo.
- **Riesgos:** No ahorrar suficiente puede afectar tu futuro económico.
- **Simulación:** Ver cómo diferentes montos de ahorro impactan en 10, 20 o 30 años.
""")

    # Simulación de impacto demográfico
    st.markdown("**Simulación de impacto demográfico:**")
    ahorro_bajo = [50000*(1+interes_anual/12)**i for i in range(meses)]
    ahorro_alto = [500000*(1+interes_anual/12)**i for i in range(meses)]
    df_demo = pd.DataFrame({"Ahorro bajo 💸": ahorro_bajo, "Ahorro alto 💰": ahorro_alto})
    st.line_chart(df_demo)
    st.markdown("Comparación: si todos ahorran poco vs. si ahorran más, la sostenibilidad cambia.")

# -----------------------------
# Tab 4: Consejos personalizados
# -----------------------------
with tab4:
    st.subheader("📝 Consejos personalizados")
    if objetivo == "Viaje ✈️":
        st.markdown(f"Si ahorras ${ahorro_mensual:,.0f} al mes, en {años} años podrías financiar tu viaje.")
    elif objetivo == "Finca raíz / apartamento 🏡":
        st.markdown(f"Si ahorras ${ahorro_mensual:,.0f} al mes, en {años} años podrías reunir la cuota inicial de un apartamento.")
    else:
        st.markdown(f"Tu ahorro mensual de ${ahorro_mensual:,.0f} te ayudará a crecer tu capital a largo plazo.")
    if edad < 30:
        st.markdown("💡 Aprovecha la juventud para empezar a invertir temprano y aprovechar el interés compuesto.")
    else:
        st.markdown("💡 Entre más pronto comiences a invertir, más fácil será alcanzar tus metas a largo plazo.")
