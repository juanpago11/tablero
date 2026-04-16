import streamlit as st
from streamlit_drawable_canvas import st_canvas

# 🎯 Título personalizado
st.title("🎨 Super Tablero")
st.subheader("Dibuja en él ✏️")

st.image("mickey.jpg", caption="Mi tablero creativo", use_container_width=True)

with st.sidebar:
    st.subheader("⚙️ Propiedades del Tablero")

    # Dimensiones
    st.markdown("### 📐 Dimensiones")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)

    # Herramientas
    st.markdown("### 🛠️ Herramientas")

    herramienta = st.selectbox(
        "Selecciona herramienta:",
        ("Dibujar", "Línea", "Rectángulo", "Círculo", "Mover", "Polígono", "Punto", "Borrador"),
    )

    # Mapear nombres bonitos a los modos reales
    modos = {
        "Dibujar": "freedraw",
        "Línea": "line",
        "Rectángulo": "rect",
        "Círculo": "circle",
        "Mover": "transform",
        "Polígono": "polygon",
        "Punto": "point",
        "Borrador": "freedraw",  # 👈 truco para borrar
    }

    drawing_mode = modos[herramienta]

    # Grosor
    stroke_width = st.slider("Tamaño del trazo", 1, 30, 15)

    # Colores
    st.markdown("### 🎨 Colores")
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")
    bg_color = st.color_picker("Color de fondo", "#000000")

# 👇 Lógica del borrador
if herramienta == "Borrador":
    stroke_color = bg_color  # pinta del mismo color del fondo

# Canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)
