#creo la clase nodo para con el poder operar los nodos
class Nodo:
    #creo el constructor para poder empezar a pasar los parametros del nodo
    def __init__(self,dato,atras=None,siguiente=None):
        self.dato=dato;
        #creo dos punteros porque el doble enlace me indica que debo señalar a los dos lados
        self.atras = atras;
        self.siguiente = siguiente;

#creo la clase lista pra alli generar las funciones que aran funcionar al codigo
class Listadobleenlace:
    def __init__(self):
        #creo la cabeza y la cola que son los punteros que voy a moverlos
        self.inicio = None;
        self.fin = None;

    #funcion para poder ingresar elementos en la cabeza
    def insertarinicio(self,dato):
        #compruebo que no este vacia la lista
        if(self.inicio==None):
            #de estarlo le paso el objeto nodo con el dato y sus punteros que son null por defecto
            self.nodo = Nodo(dato,self.inicio,self.fin);
            #el objeto le cargo en el inicio
            self.inicio = self.nodo;
            #y este a su vez en el fin, como ha estado vacia se le puede agregar elementos iguales a los dos
            self.fin = self.inicio;
        else:
            #si ya tienen datos las cosas cambian
            #creo un nuevo nodo con el dato, a lado de atras le debo dejar null, y a la derecha debo dejar los datos
            #que podrian estar trayendo ya de lado derecho
            self.nodo = Nodo(dato,None,self.inicio);
            #muevo el apuntador del inicio y que apunte hacia atras al nuevo nodo creado
            self.inicio.atras = self.nodo;
            #luego muevo el puntero hacia atras y con eso ya se coló el nuevo nodo al lado derecho de la lista
            self.inicio=self.nodo;
        
    #funcion para poder ingresar datos al final
    def insertarfinal(self,dato):
        #compruebo la lista si esta vacia
        if(self.fin==None):
            # si esta vacia croe un nuevo nodo con el elemento y los punteros de izq y der con null porque por defecto son asi
            self.nodo = Nodo(dato,self.fin,self.inicio);
            #a los dos punteros les cargo el dato del nuevo nodo
            self.fin = self.nodo;
            self.inicio = self.fin;
        else:
            #si ya tiene datos es lo inverso de la anterior funcion
            #creo nuevo nodo con el dato, de lado izquiero le paso los dayos ya existentes y del derecho le paso el null
            self.nodo = Nodo(dato,self.fin,None);
            #asi el puntero a derecha de fin le digo que señale al nuevo nodo creado
            self.fin.siguiente=self.nodo;
            #luego muevo el puntero fin al nuevo nodo
            self.fin = self.nodo;


    #funcion para comprobar la existencia de un dato
    def existenumero(self,dato):
        #cargo los datos en el  auxiliar
        self.auxiliar=self.inicio;
        #compruebo que no este vacio
        if(self.auxiliar==None):
            return 0;
        else:
            #si tiene datos le digo que los controle por recorrido
            while(self.auxiliar!=None):
                if(self.auxiliar.dato==dato):
                    #si existe me retorne 1
                    return 1;
                self.auxiliar=self.auxiliar.siguiente;
            #si no lo encontro le digo que me retorne 0
            return 0;
    
    #funcion para insertar un numero luego de un numero cualquiera
    def colocarluegode(self,numero,dato):
        #creo el nuevo nodo
        self.nodo = Nodo(dato,None,None);
        #cargo el nodo en el auxiliar
        self.auxiliar=self.inicio;
        #compruebo si entreso esta vacia
        if(self.auxiliar==None):
            print("la lista esta vacia no hay donde ingresar el elemento");
        else:
            #ccompruebo si existe el numero dentro de la lista
            if(self.existenumero(numero)==1):
                #si cumple la condicion empiezo a recorrer la lista
                while(self.auxiliar!=None):
                    if(self.auxiliar.dato==numero):
                        if(self.auxiliar==self.fin):
                            #esta condicional es en caso que sea el ultimo elemento en la lista el buscado 
                            #y le reutilizo la funcion de insertar al final
                            self.insertarfinal(dato);
                            return
                        #cuando le encuentre al dato le digo que el apuntador del nuevo a siguiente apunte hacia el sig de aux
                        self.nodo.siguiente=self.auxiliar.siguiente;
                        #el nodo hacia atras apunte al aux
                        self.nodo.atras=self.auxiliar;
                        #el sig de aux apunte al nuevo nodo
                        self.auxiliar.siguiente=self.nodo;
                        #completada la insercion le digo que ya regrese
                        return;
                    #recorro hacia adelante hasta encontrar el valor
                    self.auxiliar=self.auxiliar.siguiente;
            print("no existe ese numero dentro de la lista")
 
    #funcion para eliminar la cabeza de la lista
    def eliminarcabeza(self):
        #reviso si la lista esta vacia
        if(self.inicio==None):
            print("lista vacia no se puede eiminar ninguno");
        else:
            #reviso si la lista tiene un solo elemento entonces se borra todo por completo
            if(self.tamanio()==1):
                self.inicio=None;
                self.fin = None
            else:
                #sino cargo los datos en un auxiliar
                self.auxiliar = self.inicio;
                #al inicio le digo que almacene desde el siguiente del auxiliar
                self.inicio = self.auxiliar.siguiente;
                #la nuev posicion le digo que apunte hacia atras a null
                self.inicio.atras = None;
                #por seguridad el auxiliar lo apunto a null y lo dejo vaciado
                self.auxiliar = None;
    
    #funciona para eliminar la cola de la lista
    def eliminarcola(self):
        #compruebo que la lista este o no vacia
        if(self.fin==None):
            print("lista vacia no se puede eliminar ninguno");
        else:
            #si queda un elemento ya se le debe vaciar
            if(self.tamanio()==1):
                self.fin = None;
                self.inicio=None;
            else:
                #de lo contrario al auxiliar carga los datos
                self.auxiliar = self.fin;
                #el nodo fin es igual al apuntador de atras que tiene el auxiliar
                self.fin = self.auxiliar.atras;
                #el nuevo nodo en su siguiente le digo que apunte a null, porque recuerden que es la ultima posicion
                self.fin.siguiente = None;
                #le dejo vacio al auxiliar para que no este entreso por alli degana navegando
                self.auxiliar = None;
    
    #funcion para eliminar por posicion
    def eliminarpornumero(self,numero):
        #cargo en el auxiliar todos los datos
        self.auxiliar1=self.inicio;
        #creo el auxiliar2 que en si sera el que seguira al nodo en una posicion por detras luego
        self.auxiliar2=None;
        #compruebo que si existe dentro de la lista el numero que me piden
        if(self.existenumero(numero)==0):
            print("no existe el numero en la lista");
        else:
            while(self.auxiliar1!=None):
                #recorro el auxiliar
                if(self.auxiliar1 == self.fin):
                        #si se parecen en la parte final ingreso aqui y reutilizo la funcion de aliminar la cola 
                        self.eliminarcola();
                        return;
                else:
                    if(self.auxiliar1.dato==numero and self.auxiliar1.dato==self.inicio.dato):
                        #si se parecen en la primera posicion le reutilizo la funcion de alimnar la cabeza
                        self.eliminarcabeza();
                        return;
                    else:
                        if(self.auxiliar1.dato==numero):
                            #si no an cumplido los dos extremos entonces esta dentro asi que opero
                            #el auxiliar 2 trae la posicion anterior, asi que cambio este apuntador hacia el siguiente
                            #del auxiliar1 
                            self.auxiliar2.siguiente=self.auxiliar1.siguiente;
                            #y el siguiente del auxiliar uno tiene un puntero atras, este la cambio a que vaya hacia el aux2
                            self.auxiliar1.siguiente.atras=self.auxiliar2;
                            return;
                #aqui es donde juego con la posicion para que el aux2 le siga un nodo por detras al aux1
                self.auxiliar2=self.auxiliar1;
                #el aux1 siempre tomra un siguiente porque lo recorro apuntado al siguiente
                self.auxiliar1=self.auxiliar1.siguiente;
            
    #funcion para editar un numero por dentro
    def editarpornumero(self,numero,dato):
        #creo el nodo nuevo
        self.nodo = Nodo(dato,None,None);
        #cargo los datos en un auxiliar
        self.auxiliar = self.inicio;
        #comprobar si el numero que quiere editar existe
        if(self.existenumero(numero)==1):
            #recorro la lista en busca del numero para cambiarlo
            while(self.auxiliar!=None):
                if(self.auxiliar.dato==numero):
                    #si encuentro el dato le digo que la lista en su posicion le reemplace por el nuevo dato
                    self.auxiliar.dato=self.nodo.dato;
                    #echo el trabajo ya le digo que salga
                    return;
                #cambio las posiciones de la lista
                self.auxiliar=self.auxiliar.siguiente;
    #funcion para medir el tamaño de la lista
    def tamanio(self):
        #cargo los nodos en un auxiliar
        self.auxiliar = self.inicio;
        if(self.auxiliar==None):
            #si esta vacia me debe retomar cero
            return int(0);
        else:
            contador = int(0);
            #si esta con datos debo recorrerle hasta terminar y el contador aumentar en uno
            while(self.auxiliar!=None):
                self.auxiliar=self.auxiliar.siguiente;
                contador=contador+1;
            return contador;

    #funcion para poder leer los datos
    def leerdatos(self):
        #le cargo el inicio en el auxiliar y luego le recorro para que muestre los datos en la lectura
        self.auxiliar = self.inicio;
        if(self.auxiliar == None):
            print("las lista doble esta vacia");
        else:
            print("null", end="");
            while(self.auxiliar !=None):
                print("<-- [",self.auxiliar.dato,"] -->", end="");
                self.auxiliar = self.auxiliar.siguiente;
        print("null")

    #funcion para leer de izquierda a derecha
    def leerizqader(self):
        #aqui es igual que la lectura normal, porque le paso al auxiliar los datos y este recorre hacia la derecha
        #con el puntero
        self.auxiliar = self.inicio;
        if(self.auxiliar == None):
            print("las lista doble esta vacia");
        else:
            print("null", end="");
            while(self.auxiliar !=None):
                print("<-- [",self.auxiliar.dato,"] -->", end="");
                self.auxiliar = self.auxiliar.siguiente;
        print("null");

    #funcion para leer de derecha a izquierda
    def leerderaizq(self):
        #aqui le paso auxiliar el nodo fin, para que al recorrer el puntero señale hacia la izquierda
        #y segun corre la lectura los datos van pasando a la lectura
        self.auxiliar = self.fin;
        if(self.auxiliar == None):
            print("las lista doble esta vacia");
        else:
            print("null", end="");
            while(self.auxiliar !=None):
                print("<-- [",self.auxiliar.dato,"] -->", end="");
                self.auxiliar = self.auxiliar.atras;
        print("null")
        
#creo el objeto para poder leer los datos
lista = Listadobleenlace();
paso = True;
while(paso):
    print("------Opciones------")
    print("1 presione para ingresar datos en la cabeza de lista");
    print("2 presione para ingresar datos en la cola de lista");
    print("3 presione para ver lecturas izq-der y der-izq de la lista");
    print("4 ingresar nuevo nodo luego de un numero");
    print("5 editar un numero de la lista");
    print("6 eliminar elemento de cabeza");
    print("7 eliminar elemento de cola");
    print("8 eliminar por numero buscado dentro de la lista");
    numero = int(input("0 Para salir del programa: "));
    if(numero==1):
        print("");
        dato = int(input("ingrese el elemento en la cabeza: "));
        lista.insertarinicio(dato);
    elif(numero==0):
        paso=False;
    elif(numero==2):
        print("");
        dato = int(input("ingrese el elemento en la cola: "));
        lista.insertarfinal(dato);
    elif(numero==3):
        print("");
        print("Lectura de izquierda a derecha de los datos: ");
        lista.leerizqader();
        print("Lextura de derecha a izquierda de los datos: ");
        lista.leerderaizq();
    elif(numero==4):
        print("");
        numero = int(input("detras de cual numero quiere colocar el nuevo: "));
        dato = int(input("ingrese el nuevo nodo: "));
        lista.colocarluegode(numero,dato);
    elif(numero==5):
        numero = int(input("ingrese el numero que desea editar: "));
        dato = int(input("ingrese el nuevo numero: "));
        lista.editarpornumero(numero,dato);
    elif(numero==6):
        print("");
        lista.eliminarcabeza();
    elif(numero==7):
        print("");
        lista.eliminarcola();
    elif(numero==8):
        print("");
        numero = int(input("que numero desea eliminar de la lista: "));
        lista.eliminarpornumero(numero);
    print("");
    print("Elementos guardados en la lista");
    lista.leerdatos();
    print("Tamanio de la lista: ",lista.tamanio());
    print("");

