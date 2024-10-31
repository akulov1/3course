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
            double[] gr_sum = new double[numofprevneurons+1];
            //код обучения нейросети
            return gr_sum;
        }
    }
}
