import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.image as mpimg

pdf_path = "Anotop_diapositivas.pdf"

with PdfPages(pdf_path) as pdf:
    # ------------------ SLIDE 1: PORTADA & LA PREGUNTA ------------------
    fig = plt.figure(figsize=(11, 6.18), facecolor='#f8f9fa')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    
    # Header banner
    ax.fill_between([0, 1], [0.82, 0.82], [1, 1], color='#1a365d')
    ax.text(0.06, 0.90, "DATATÓN TECH FOR GOOD · INNOSOFT 26–27", color='#63b3ed', fontsize=12, fontweight='bold', va='center')
    ax.text(0.06, 0.85, "ETSII · Universidad de Sevilla", color='#e2e8f0', fontsize=10, va='center')
    ax.text(0.94, 0.88, "Equipo: ANOTOP", color='#ffffff', fontsize=16, fontweight='bold', ha='right', va='center')
    
    # Title & Question
    ax.text(0.06, 0.68, "Desmontando el factor jornada en la brecha salarial", color='#2d3748', fontsize=22, fontweight='bold')
    
    # Question card
    ax.fill_between([0.06, 0.94], [0.35, 0.35], [0.58, 0.58], color='#edf2f7', edgecolor='#cbd5e0', linewidth=1.5)
    ax.text(0.09, 0.52, "LA PREGUNTA DE INVESTIGACIÓN:", color='#4a5568', fontsize=11, fontweight='bold')
    ax.text(0.09, 0.43, "¿Cuánto de la brecha salarial bruta en Andalucía responde realmente a una\ndiferencia de salario a igual trabajo y cuánto a la diferencia de horas trabajadas?", 
            color='#1a202c', fontsize=14, fontweight='bold', style='italic')
    
    # Key takeaways
    ax.text(0.06, 0.22, "• Integrantes: Juan · Nico · Paco", color='#4a5568', fontsize=12)
    ax.text(0.06, 0.15, "• Hallazgo clave: Más del 56% de la brecha bruta anual desaparece al comparar a tiempo completo.", color='#2b6cb0', fontsize=12, fontweight='bold')
    ax.text(0.06, 0.08, "• Fuentes: IECA (MCVL 2024 · DS-005) y Microdatos calibrados Sector TIC (DS-013).", color='#718096', fontsize=10)
    
    pdf.savefig(fig, dpi=150)
    plt.close()

    # ------------------ SLIDE 2: DATOS Y MÉTODO ------------------
    fig = plt.figure(figsize=(11, 6.18), facecolor='#f8f9fa')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    
    ax.fill_between([0, 1], [0.86, 0.86], [1, 1], color='#1a365d')
    ax.text(0.06, 0.93, "2 · DATOS Y METODOLOGÍA RIGUROSA", color='#ffffff', fontsize=16, fontweight='bold', va='center')
    ax.text(0.94, 0.93, "Equipo ANOTOP", color='#cbd5e0', fontsize=11, ha='right', va='center')
    
    # Box 1: Datos Oficiales
    ax.fill_between([0.06, 0.48], [0.15, 0.15], [0.80, 0.80], color='#ffffff', edgecolor='#e2e8f0', linewidth=1.5)
    ax.text(0.09, 0.74, "1. Datos Oficiales Macro (Andalucía)", color='#2b6cb0', fontsize=13, fontweight='bold')
    ax.text(0.09, 0.67, "• IECA · MCVL 2024 (DS-005):", color='#2d3748', fontsize=11, fontweight='bold')
    ax.text(0.11, 0.61, "- Salario bruto anual vs. eq. tiempo completo.\n- Comparación Media vs. Mediana (persona típica).", color='#4a5568', fontsize=10)
    ax.text(0.09, 0.50, "• Validación Oficial (DS-012):", color='#2d3748', fontsize=11, fontweight='bold')
    ax.text(0.11, 0.44, "- Verificación al 100% con las 2 fórmulas:\n   (H - M) / H   y   (H / M) - 1.", color='#4a5568', fontsize=10)
    ax.text(0.09, 0.30, "• Salario por Edad (DS-004):", color='#2d3748', fontsize=11, fontweight='bold')
    ax.text(0.11, 0.24, "- Análisis del ensanchamiento de la brecha\n  a partir de los 30 años.", color='#4a5568', fontsize=10)
    
    # Box 2: Microdatos y Modelo Econométrico
    ax.fill_between([0.52, 0.94], [0.15, 0.15], [0.80, 0.80], color='#ffffff', edgecolor='#e2e8f0', linewidth=1.5)
    ax.text(0.55, 0.74, "2. Microdatos TIC y Modelo Econométrico", color='#2b6cb0', fontsize=13, fontweight='bold')
    ax.text(0.55, 0.67, "• Simulación TIC (DS-013, 3.000 obs):", color='#2d3748', fontsize=11, fontweight='bold')
    ax.text(0.57, 0.61, "- Descomposición matemática: efecto salario/hora\n  vs. efecto horas semanales.", color='#4a5568', fontsize=10)
    ax.text(0.55, 0.50, "• Ecuación de Mincer (Regresión log-lineal):", color='#2d3748', fontsize=11, fontweight='bold')
    ax.text(0.57, 0.44, "- ln(Salario/hora) ~ Mujer + Horas + Experiencia +\n  Antigüedad + Rol técnico + Tamaño empresa.", color='#4a5568', fontsize=10)
    ax.text(0.55, 0.30, "• Calidad econométrica:", color='#2d3748', fontsize=11, fontweight='bold')
    ax.text(0.57, 0.24, "- R² = 0,444: Capacidad explicativa robusta.\n- Aisla el sesgo por rol profesional (segregación).", color='#4a5568', fontsize=10)
    
    pdf.savefig(fig, dpi=150)
    plt.close()

    # ------------------ SLIDE 3: HALLAZGOS Y GRÁFICOS ------------------
    fig = plt.figure(figsize=(11, 6.18), facecolor='#f8f9fa')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    
    ax.fill_between([0, 1], [0.86, 0.86], [1, 1], color='#1a365d')
    ax.text(0.06, 0.93, "3 · HALLAZGOS: EL FACTOR JORNADA Y EL ROL OCUPACIONAL", color='#ffffff', fontsize=16, fontweight='bold', va='center')
    ax.text(0.94, 0.93, "Equipo ANOTOP", color='#cbd5e0', fontsize=11, ha='right', va='center')
    
    # Embed images
    img1 = mpimg.imread("figuras/grafico1_efecto_jornada_andalucia.png")
    img3 = mpimg.imread("figuras/grafico3_descomposicion_regresion.png")
    
    ax1 = fig.add_axes([0.05, 0.15, 0.43, 0.68])
    ax1.imshow(img1)
    ax1.axis('off')
    
    ax2 = fig.add_axes([0.52, 0.15, 0.43, 0.68])
    ax2.imshow(img3)
    ax2.axis('off')
    
    pdf.savefig(fig, dpi=150)
    plt.close()

    # ------------------ SLIDE 4: CONCLUSIÓN, LÍMITES Y ACCIÓN ------------------
    fig = plt.figure(figsize=(11, 6.18), facecolor='#f8f9fa')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    
    ax.fill_between([0, 1], [0.86, 0.86], [1, 1], color='#1a365d')
    ax.text(0.06, 0.93, "4 · CONCLUSIÓN, LÍMITES Y ACCIÓN CONCRETA", color='#ffffff', fontsize=16, fontweight='bold', va='center')
    ax.text(0.94, 0.93, "Equipo ANOTOP", color='#cbd5e0', fontsize=11, ha='right', va='center')
    
    # 1. Conclusión en una frase
    ax.fill_between([0.06, 0.94], [0.66, 0.66], [0.80, 0.80], color='#ebf8ff', edgecolor='#90cdf4', linewidth=1.5)
    ax.text(0.08, 0.74, "CONCLUSIÓN EN UNA FRASE:", color='#2b6cb0', fontsize=11, fontweight='bold')
    ax.text(0.08, 0.69, "La mayor parte de la brecha salarial bruta en Andalucía no se debe a cobrar menos por hora,\nsino al factor jornada (parcialidad) y a la segregación ocupacional en el sector TIC.", color='#2d3748', fontsize=12, fontweight='bold')
    
    # 2. Qué NO se puede concluir (Honestidad de datos)
    ax.fill_between([0.06, 0.48], [0.10, 0.10], [0.60, 0.60], color='#fffaf0', edgecolor='#feebc8', linewidth=1.5)
    ax.text(0.09, 0.54, "⚠️ Qué NO se puede concluir", color='#c05621', fontsize=12, fontweight='bold')
    ax.text(0.09, 0.45, "• El 8,2% restante a tiempo completo NO es\n  100% discriminación salarial directa.", color='#4a5568', fontsize=10)
    ax.text(0.09, 0.35, "• Persiste segregación vertical no observable:\n  acceso desigual a puestos de alta dirección.", color='#4a5568', fontsize=10)
    ax.text(0.09, 0.23, "• Los microdatos TIC son sintéticos calibrados:\n  muestran mecanismos, no personas individuales.", color='#4a5568', fontsize=10)
    ax.text(0.09, 0.14, "• Brecha de datos: Falta cruce oficial completo\n  TIC × sexo × edad × jornada en Andalucía.", color='#718096', fontsize=9, style='italic')
    
    # 3. Propuesta de Acción Concreta
    ax.fill_between([0.52, 0.94], [0.10, 0.10], [0.60, 0.60], color='#f0fff4', edgecolor='#9ae6b4', linewidth=1.5)
    ax.text(0.55, 0.54, "🎯 Propuesta de Acción Concreta", color='#276749', fontsize=12, fontweight='bold')
    ax.text(0.55, 0.43, "Para Empresas TIC y Administraciones Públicas:", color='#2d3748', fontsize=11, fontweight='bold')
    ax.text(0.55, 0.30, "«Exigir en los convenios y planes de igualdad TIC\nla publicación obligatoria de auditorías desagregadas\npor SALARIO POR HORA EFECTIVA y tramos de jornada,\nen lugar de cifras brutas anuales agregadas.»", color='#22543d', fontsize=10, fontweight='bold')
    ax.text(0.55, 0.16, "Permitirá diagnosticar si la desigualdad proviene\nde barreras de conciliación (horas) o de techos\nde cristal en la promoción técnica interna.", color='#4a5568', fontsize=9)
    
    pdf.savefig(fig, dpi=150)
    plt.close()

print("Anotop_diapositivas.pdf generado exitosamente.")

