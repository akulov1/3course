using System;
using System.IO;
using System.Windows.Forms;

namespace _35._2_Akulov_project.NeuroNet
{
    abstract class Layer
    {
        protected string name_Layer;
        string pathDirWeights;
        string pathFileWeights;
        protected int numofneurons;
        protected int numofprevneurons;
        protected const double learningrate = 0.005d; //скорость обучения
        protected const double momentum = 0.05; //param optimization 
        protected double[,] lastdeltaweights;
        Neuron[] _neurons;

        public Neuron[] Neurons { get => _neurons; set => _neurons = value; }

        public double[] Data
        {
            set
            {
                for(int i = 0;i<Neurons.Length; i++)
                {
                    Neurons[i].Inputs = value;
                    Neurons[i].Activator(Neurons[i].Inputs, Neurons[i].Weights);
                }
            }
        }
        //constructor
        protected Layer(int non, int nonp,NeuronType nt, string nm_Layer)
        {
            numofneurons = non;
            numofprevneurons = nonp;
            Neurons = new Neuron[non];
            name_Layer = nm_Layer;
            pathDirWeights = AppDomain.CurrentDomain.BaseDirectory + "memory\\"; // path to catalog
            pathFileWeights = pathDirWeights + name_Layer + "_memory.csv"; //path to file with synaptics weights
            double[,] Weights;
            if (File.Exists(pathFileWeights))
            {
                Weights = WeightInitialize(MemoryMode.GET, pathFileWeights);
            }
            else
            {
                Directory.CreateDirectory(pathDirWeights);
                Weights = WeightInitialize(MemoryMode.INIT, pathFileWeights);
            }

            lastdeltaweights = new double[non, nonp + 1];
            for (int i = 0; i<non; i++)
            {
                double[] tmp_weights = new double[nonp + 1];
                for(int j= 0; j<nonp+1; j++)
                {
                    tmp_weights[j] = Weights[i, j];
                }
                Neurons[i] = new Neuron(tmp_weights, nt);
            }
        }

        public double[,] WeightInitialize(MemoryMode mm, string path)
        {
            int i, j;
            char[] delim = new char[] { ';', ' ' };
            string tmpStr;
            string[] tmpStrWeights;
            double[,] weights = new double[numofneurons, numofprevneurons + 1];

            switch (mm)
            {
                case MemoryMode.GET:
                    tmpStrWeights = File.ReadAllLines(path);
                    string[] memory_element;
                    for (i = 0; i<numofneurons; i++)
                    {
                        memory_element = tmpStrWeights[i].Split(delim);
                        for (j=0; j<numofprevneurons+1; j++)
                        {
                            weights[i, j] = double.Parse(memory_element[j].Replace(',', '.'), System.Globalization.CultureInfo.InvariantCulture);
                        }
                    }
                    break;

                case MemoryMode.SET:
                    break;

                case MemoryMode.INIT:
                    break;
            }
            return weights;
        }
        //для прямых проходов
        abstract public void Recognize(Network net, Layer nextLayer);
        //для обратных проходов
        abstract public double[] BackwardPass(double[] stuff);
    }//прописать инициализацию и сохранение! 
}
