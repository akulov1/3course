namespace _35._2_Akulov_project.NeuroNet
{
    class HiddenLayer : Layer
    {
        //constructor
        public HiddenLayer(int non, int nonp, NeuronType nt, string type): base(non, nonp, nt, type) { }

        public override void Recognize(Network net, Layer nextLayer)
        {
            double[] hidden_out = new double[Neurons.Length];

            for (int i = 0; i<Neurons.Length; i++)
            {
                hidden_out[i] = Neurons[i].Output;
            }
            nextLayer.Data = hidden_out;
        }

        public override double[] BackwardPass(double[] stuff)
        {
            double[] gr_sum = new double[numofprevneurons];
            //код обучения нейросети
            return gr_sum;
        }
    }
}
