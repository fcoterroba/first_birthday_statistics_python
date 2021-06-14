import matplotlib.pyplot as plt

# Make the arrays with the info
meses = ["Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre", "Enero", "Febrero", "Marzo"]
visitas = [816, 1034, 1101, 1250, 1604, 1983, 2468, 3021, 2867, 3520, 4010, 5097]

# Make the arrays with trimester data
months = ["1º trimestre: Abril-Junio", "2º trimestre: Julio-Septiembre", "3º trimestre: Octubre-Diciembre", "4º trimestre: Enero-Marzo"]
visits_trimester = [2951, 4837, 8356, 12627]

def grafico_barra_vertical():

    # Make the object
    fig, ax = plt.subplots()
    
    # Label for Y
    ax.set_ylabel('Visitas')
    # Label for X
    ax.set_title('Visitas en el primer aniversario de la web')
    
    # Set the arrays to the X and Y
    plt.bar(meses, visitas)
    
    # Show the chart
    plt.show()

def grafico_lineas_horizontal(): 

    # Make a plot with data
    plt.plot(meses, visitas)

    # Show the chart
    plt.show()

def grafico_tarta_trimestral():

    # Make a plot with the data and labels
    plt.pie(visits_trimester, labels = months)
    plt.show()


if __name__ == "__main__":
    grafico_barra_vertical()
    grafico_lineas_horizontal()
    grafico_tarta_trimestral()
