#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

namespace py = pybind11;

// Función para sumar números flotantes
double sum_floats(const std::vector<double>& numbers) {
    double sum = 0.0;
    for (double num : numbers) {
        sum += num;
    }
    return sum;
}

int contador(int total){
    //float temp = 0.0;
    int i=total;
    for (; i > 0; i--) {
    	sqrt(i);
    }	
    return i;
}

double avg_floats(const std::vector<double>& numbers) {
    double sum = 0.0;
    int cc = 0;
    for (double num : numbers) {
        sum += num;
        cc++;
    }
    double avg = sum / cc;
    return avg;
}



// Enlace de la función sum_floats a Python usando pybind11
PYBIND11_MODULE(suma, m) {
    m.def("contador", &contador, "Suma una lista de números flotantes");
    m.def("sum_floats", &sum_floats, "Suma una lista de números flotantes");
    m.def("avg_floats", &avg_floats, "Suma una lista de números flotantes y obtiene la media");
}

