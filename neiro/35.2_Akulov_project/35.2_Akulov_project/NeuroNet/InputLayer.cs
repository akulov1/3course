using System;
using System.IO;

namespace _35._2_Akulov_project.NeuroNet
{
    class InputLayer
    {
        private Random random = new Random();

        //polya
        private double[,] trainset = new double[100, 16];
        private double[,] testset = new double[10, 16];

        public double[,] TrainSet { get => trainset; }
        public double[,] TestSet { get => testset; }

        public InputLayer(NetworkMode nm)
        {
            string path = AppDomain.CurrentDomain.BaseDirectory;
            string[] tmpStr;
            string[] tmpArrStr;
            double[] tmpArr;

            switch (nm)
            {
                case NetworkMode.Train:
                    tmpArrStr = File.ReadAllLines(path + "train.txt");
                    for (int i = 0; i<tmpArrStr.Length; i++)
                    {
                        tmpStr = tmpArrStr[i].Split();
                        tmpArr = new double[tmpStr.Length];
                        for (int j = 0; j<tmpStr.Length; j++)
                        {
                            tmpArr[j] = double.Parse(tmpStr[j], System.Globalization.CultureInfo.InvariantCulture);
                        }
                    }

                    for(int n = trainset.GetLength(0)-1; n >= 1; n--)
                    {
                        int j = random.Next(n + 1);
                        double[] temp = new double[trainset.GetLength(1)];

                        for (int i =0; i< trainset.GetLength(1); i++)
                        {
                            temp[i] = trainset[n,i];
                        }
                        for(int i =0; i < trainset.GetLength(1); i++)
                        {
                            trainset[n, i] = trainset[j, i];
                            trainset[j,i] = temp[i];
                        }

                    }

                    break;
                
                case NetworkMode.Test:
                    tmpArrStr = File.ReadAllLines(path + "test.txt");
                    for (int i = 0; i < tmpArrStr.Length; i++)
                    {
                        tmpStr = tmpArrStr[i].Split();
                        for (int j = 0; j < tmpStr.Length; j++)
                        {
                            testset[i, j] = double.Parse(tmpStr[j], System.Globalization.CultureInfo.InvariantCulture);
                        }
                    }
                    break;
                case NetworkMode.Recognise:
                    break;
            }
        }
    }
}
