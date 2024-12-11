using System;

namespace _35._2_Akulov_project.NeuroNet
{
    class Network
    {
        //sloi
        private InputLayer input_layer = null;
        private HiddenLayer hidden_layer1 = new HiddenLayer(70, 15, NeuronType.Hidden, nameof(hidden_layer1));
        private HiddenLayer hidden_layer2 = new HiddenLayer(31, 70, NeuronType.Hidden, nameof(hidden_layer2));
        private OutputLayer output_layer = new OutputLayer(10, 31, NeuronType.Output, nameof(output_layer));

        public double[] fact = new double[10];

        private double[] e_error_avr;//среднее значение энергии ошибки эпохи обучения

        public double[] E_error_avr { get => e_error_avr; set => e_error_avr = value; } //срденне значение энергии эпохи обучения
        
        public Network() { }

        public void Train(Network net)
        {
            int epoches = 100;
            net.input_layer = new InputLayer(NetworkMode.Train);//инициализация вх слоя
            double tmpSumError;
            double[] errors;//массив сигнала ошибки
            double[] temp_gsums1; //градиент первого слоя
            double[] temp_gsums2;
            double[] temp3;
            e_error_avr = new double[epoches];
            double[,] hiddenLayer1Weights = new double[70, 15];
            double[,] hiddenLayer2Weights = new double[31, 70];
            double[,] outputLayerWeights = new double[10, 31];

            for (int k = 0; k < epoches; k++)//перебор эпох обучения
            {
                e_error_avr[k] = 0;//обновление энергии ошибки
                for (int i = 0; i < net.input_layer.TrainSet.GetLength(0); i++)
                {
                    double[] tmpTrain = new double[15];
                    for (int j = 0; j < tmpTrain.Length; j++)
                        tmpTrain[j] = net.input_layer.TrainSet[i, j + 1];
                    ForwardPass(net, tmpTrain);

                    tmpSumError = 0;
                    errors = new double[net.fact.Length];
                    for (int x = 0; x < errors.Length; x++)
                    {
                        if (x == net.input_layer.TrainSet[i, 0])
                            errors[x] = 1-net.fact[x];
                        else
                            errors[x] = -net.fact[x];

                        tmpSumError += errors[x] * errors[x] / 2;
                    }
                    e_error_avr[i] += tmpSumError / errors.Length;
                    //обратный проход и коррекция весов
                    temp_gsums2 = net.output_layer.BackwardPass(errors);
                    temp_gsums1 = net.hidden_layer2.BackwardPass(temp_gsums2);
                    temp3 = net.hidden_layer1.BackwardPass(temp_gsums1);

                }
                e_error_avr[k] /= net.input_layer.TrainSet.GetLength(0); // Средняя энергия ошибки k-ой эпохи
            }
            net.input_layer = null;
            SaveWeights();
        }
        
        private void SaveWeights()
        {
            string pathBase = AppDomain.CurrentDomain.BaseDirectory + "memory\\";
            hidden_layer1.WeightInitialize(MemoryMode.SET, pathBase + "hidden_layer1_memory.csv", GetWeights(hidden_layer1));
            hidden_layer2.WeightInitialize(MemoryMode.SET, pathBase + "hidden_layer2_memory.csv", GetWeights(hidden_layer2));
            output_layer.WeightInitialize(MemoryMode.SET, pathBase + "output_layer_memory.csv", GetWeights(output_layer));
        }
        
        private double[,] GetWeights(Layer layer)
        {
            double[,] weights = new double[layer.Neurons.Length, layer.Neurons[0].Weights.Length];
        
            for (int i = 0; i < layer.Neurons.Length; i++)
            {
                for (int j = 0; j < layer.Neurons[i].Weights.Length; j++)
                {
                    weights[i, j] = layer.Neurons[i].Weights[j];
                }
            }
        
            return weights;
        }
        
        public void ForwardPass(NetWork net, double[] netInput)
        {
            net.hidden_layer1.Data = netInput;
            net.hidden_layer1.Recognize(null, net.hidden_layer2);
            net.hidden_layer2.Recognize(null, net.output_layer);
            net.output_layer.Recognize(net, null);
        }
    }
}
