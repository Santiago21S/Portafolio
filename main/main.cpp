#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

// Estructura para almacenar los registros de la bitácora
struct Registro {
  string mes;
  int dia;
  string hora;
  string ip;
  int puerto;  // Separamos el puerto de la IP
  string razon;

  // Función para extraer la parte de la IP (sin el puerto)
  string extraerIP() const {
    size_t posicion = ip.find(':');
    return ip.substr(0, posicion);
  }

  // Función para comparar direcciones IP
  bool operator<(const Registro &otro) const {
    if (extraerIP() == otro.extraerIP()) {
      return puerto < otro.puerto;
    }
    return extraerIP() < otro.extraerIP();
  }

  bool operator>(const Registro &otro) const {
    if (extraerIP() == otro.extraerIP()) {
      return puerto > otro.puerto;
    }
    return extraerIP() > otro.extraerIP();
  }

  bool operator>=(const Registro &otro) const {
    if (extraerIP() == otro.extraerIP()) {
      return puerto >= otro.puerto;
    }
    return extraerIP() >= otro.extraerIP();
  }

  bool operator<=(const Registro &otro) const {
    if (extraerIP() == otro.extraerIP()) {
      return puerto <= otro.puerto;
    }
    return extraerIP() <= otro.extraerIP();
  }
};

// Función para dividir una línea de texto en partes
vector<string> dividirLinea(string linea) {
  vector<string> partes;
  stringstream ss(linea);
  string item;
  while (ss >> item) {
    partes.push_back(item);
  }
  return partes;
}

// Función para extraer el puerto de una dirección IP con puerto
int extraerPuerto(string ipConPuerto) {
  size_t posicion = ipConPuerto.find(':');
  return stoi(ipConPuerto.substr(posicion + 1));
}

// Leer archivo de bitácora y almacenar registros en un vector
vector<Registro> leerBitacora(string nombreArchivo) {
  ifstream archivo(nombreArchivo);
  vector<Registro> bitacora;
  string linea;

  while (getline(archivo, linea)) {
    vector<string> partes = dividirLinea(linea);
    if (partes.size() >= 5) {
      // Extraer IP y puerto
      string ipCompleta = partes[3];
      int puerto = extraerPuerto(ipCompleta);

      Registro reg = {partes[0], stoi(partes[1]), partes[2], ipCompleta, puerto,
                      partes[4]};
      bitacora.push_back(reg);
    }
  }
  archivo.close();
  return bitacora;
}

// Algoritmo de ordenamiento por inserción
void ordenarPorInsercion(vector<Registro> &bitacora) {
  int n = bitacora.size();
  for (int i = 1; i < n; i++) {
    Registro key = bitacora[i];
    int j = i - 1;

    // Mover los elementos mayores que key una posición adelante
    while (j >= 0 && bitacora[j] > key) {
      bitacora[j + 1] = bitacora[j];
      j--;
    }
    bitacora[j + 1] = key;
  }
}

// Guardar los registros en un archivo ordenado
void guardarBitacoraOrdenada(vector<Registro> bitacora, string nombreArchivo) {
  ofstream archivo(nombreArchivo);
  for (int i = 0; i < bitacora.size(); i++) {
    archivo << bitacora[i].mes << " " << bitacora[i].dia << " "
            << bitacora[i].hora << " " << bitacora[i].ip << " "
            << bitacora[i].razon << endl;
  }
  archivo.close();
}

// Función para solicitar IPs al usuario (incluyendo el puerto)
void solicitarIPs(string &IPInicio, string &IPFin) {
  cout << "Ingrese la IP de inicio (formato: XXX.XXX.XXX.XXX:PORT): ";
  getline(cin, IPInicio);
  cout << "Ingrese la IP de fin (formato: XXX.XXX.XXX.XXX:PORT): ";
  getline(cin, IPFin);
}

// Función de búsqueda binaria para encontrar el primer registro en el rango
int buscarInicio(vector<Registro> bitacora, Registro IPInicio) {
  int izquierda = 0;
  int derecha = bitacora.size() - 1;
  while (izquierda <= derecha) {
    int medio = (izquierda + derecha) / 2;
    if (bitacora[medio] >= IPInicio) {
      derecha = medio - 1;
    } else {
      izquierda = medio + 1;
    }
  }
  return izquierda;
}

// Función de búsqueda binaria para encontrar el último registro en el rango
int buscarFin(vector<Registro> bitacora, Registro IPFin) {
  int izquierda = 0;
  int derecha = bitacora.size() - 1;
  while (izquierda <= derecha) {
    int medio = (izquierda + derecha) / 2;
    if (bitacora[medio] <= IPFin) {
      izquierda = medio + 1;
    } else {
      derecha = medio - 1;
    }
  }
  return derecha;
}

// Función para mostrar registros en el rango de IPs
void mostrarRegistrosEnRango(vector<Registro> bitacora, string inicio,
                             string fin) {
  // Crear registros con las IPs de inicio y fin
  int puertoInicio = extraerPuerto(inicio);
  int puertoFin = extraerPuerto(fin);
  Registro IPInicio = {"", 0, "", inicio, puertoInicio, ""};
  Registro IPFin = {"", 0, "", fin, puertoFin, ""};

  // Buscar los índices usando búsqueda binaria
  int indiceInicio = buscarInicio(bitacora, IPInicio);
  int indiceFin = buscarFin(bitacora, IPFin);

  cout << "Registros entre " << inicio << " y " << fin << ":" << endl;

  // Imprimir los registros en el rango
  for (int i = indiceInicio; i <= indiceFin; i++) {
    cout << bitacora[i].mes << " " << bitacora[i].dia << " " << bitacora[i].hora
         << " " << bitacora[i].ip << " " << bitacora[i].razon << endl;
  }
}

int main() {
  // Leer bitácora
  vector<Registro> bitacora = leerBitacora("bitacora.txt");

  // Ordenar la bitácora por IP
  ordenarPorInsercion(bitacora);

  // Guardar bitácora ordenada
  guardarBitacoraOrdenada(bitacora, "bitacora_ordenada_por_ip2.txt");

  // Solicitar IPs al usuario
  string IPInicio, IPFin;
  solicitarIPs(IPInicio, IPFin);

  // Mostrar registros en el rango de IPs
  mostrarRegistrosEnRango(bitacora, IPInicio, IPFin);

  return 0;
}
