using System;
using static System.Math;

namespace _35._2_Akulov_project.NeuroNet
{
    class Neuron
    {
        private NeuronType type;//type of neuron
        private double[] _weights;
        private double[] _inputs;
        private double _output;
        private double _derivative; //производная функции активации
        private double a = 0.01; //const для функции активации

        public double[] Weights{ get => _weights; set => _weights = value; }
        public double[] Inputs { get => _inputs; set => _inputs = value; }
        public double Output { get => _output; }
        public double Derivative { get => _derivative; }

        public Neuron(double[] weigths, NeuronType type)
        {
            this.type = type;
            _weights = weigths;
        }

        public void Activator(double[] inputs, double[] w)
        {
            _inputs = inputs;
            double sum = w[0];
            for (int m = 0; m < _inputs.Length; m++)
            {
                sum += _inputs[m] * _weights[m + 1];
            }

            // Уравнение логистической функции: f(x) = 1/(1+e^(-x))
            _output = 1.0 / (1.0 + Math.Exp(-sum));

            //производная для логистической функции: f'(x) = f(x)*(1-f(x))
            _derivative = _output * (1.0 - _output);
        }

    }
}
