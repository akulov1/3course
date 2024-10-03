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
        
        // логистическая функция активации

        public double[] Weights{ get => _weights; set => _weights = value; }
        public double[] Inputs { get => _inputs; set => _inputs = value; }
        public double Output { get => _output; }
        public double Derivative { get => _derivative; }

        public Neuron(double[] weigths, NeuronType type)
        {
            this.type = type;
            _weights = weigths;
        }

        public void Activator(double[] i, double[] w)
        {
            double sum = w[0];
            for (int m = 0; m < i.Length; m++)
                sum += i[m] * w[m + 1];
        }
        //дописать код нейрона с функциями активации и составить тест и обучающую выборку

    }
}
