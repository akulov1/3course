namespace _35._2_Akulov_project.NeuroNet
{
    class OutputLayer : Layer
    {
        public OutputLayer(int non, int nonp, NeuronType nt, string type) : base(non, nonp, nt, type) { }

        public override void Recognize(Network net, Layer nextLayer)
        {
            double e_sum = 0;
            for (int i = 0; i < Neurons.Length; i++)
                e_sum += Neurons[i].Output;
            for (int i = 0; i < Neurons.Length; i++)
                net.fact[i] = Neurons[i].Output / e_sum; //выходной сигнал нейросети
        }
        public override double[] BackwardPass(double[] errors)
        {
            double[] gr_sum = new double[numofprevneurons];

            for(int j =0; j < numofprevneurons; j++)
            {
                double sum = 0;
                for (int k = 0; k < numofneurons; k++)
                    sum += _neurons[k].Weights[j] * errors[k];
                gr_sum[j] = sum;
            }

            for(int i=0; i<numofneurons;i++)
                for(int n=0; n < numofprevneurons+1; n++) {
                    double deltaw;
                    if (n == 0)
                        deltaw = momentum * lastdeltaweights[i, 0] + learningrate * errors[i];
                    else
                        deltaw = momentum * lastdeltaweights[i, n] + learningrate * _neurons[i].Inputs[n - 1] * errors[i];
                    lastdeltaweights[i, n] = deltaw;
                    _neurons[i].Weights[n] += deltaw;//correction of weights
                }

            return gr_sum;
        }
    }
}
