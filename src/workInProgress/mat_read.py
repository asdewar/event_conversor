from scipy.io import loadmat

PATH=''

def main():

    path = 'b/b_0001'
    # path = '20170214-20-58_22285_SL-16RB'
    # path = 'archenar_leos_11_33_atis_td'

    full_path = 'MAT/' + path + '.mat'

    # Cargamos los datos.
    file_data = loadmat(full_path)

    # Se imprime las estructuras de datos.
    print(file_data.keys())

    # Recogemos la estructura TD, en la cual 
    data = file_data[STRUCT_NAME]

    print(data.dtype)

    # Inicializamos las variables.
    x, y, p, ts = None, None, None, None

    x = data[0, 0]['x']
    y = data[0, 0]['y']
    p = data[0, 0]['p']
    ts = data[0, 0]['ts']

    # Intentamos decodificar los datos obtenidos desde matlab.
    # try:
    #     x = data['x'][0]
    #     y = data['y'][0]
    #     p = data['p'][0]
    #     ts = data['ts'][0]
    #     print("Decodificado como diccionario")
    # except:
    #     try:
    #         x = data[0]
    #         y = data[1]
    #         p = data[2]
    #         ts = data[3]
    #         print("Decodificado como array")
    #     except:
    #         print("No se ha podido decodificar.")
    #         return
    
    # print("Exito en la decodificación")
    print("FIN")

        

if __name__ == '__main__':
    main()
