using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using NBitcoin.DataEncoders;
using NBitcoin;
using NBitcoin.Crypto;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            byte[] brain = System.Text.Encoding.UTF8.GetBytes("Lykkex1");
            byte[] p = Hashes.SHA256(brain);
            string hexp = Encoders.Hex.EncodeData(p);
            Console.WriteLine(hexp);

            Console.WriteLine(Encoders.Base58.EncodeData(p));

            String baddr = "1NDKhcEiha89vUPuxeg5zBdg38kMh9H1JQ";
            byte[] byteArray = Encoders.Base58.DecodeData(baddr);
            string hex = Encoders.Hex.EncodeData(byteArray);
           // Console.Write(hex);

            BitcoinAddress addr = BitcoinAddress.Create(baddr);
            Key privateKey = new Key();
            BitcoinAddress addr2 = privateKey.PubKey.GetAddress(Network.Main);
            string priv = "z4tiDi9WNB933EaS4wvnGL8UByT5jEJxZRnkF6zNAWGNAyrwvgWV6pNneRbh3WNQ9qFszWhVkp3eV7Sm3SANUBh";
            byte[] arr = Encoders.Base58.DecodeData(priv);
            //Console.Write(Encoders.Hex.EncodeData(arr));
            //BitcoinSecret secret = new BitcoinSecret("z4tiDi9WNB933EaS4wvnGL8UByT5jEJxZRnkF6zNAWGNAyrwvgWV6pNneRbh3WNQ9qFszWhVkp3eV7Sm3SANUBh", Network.Main);
            //string sign = secret.PrivateKey.SignMessage("I am owner");
    
            //Console.Write("hash {0} {0}", addr.Hash, sign);
            Console.ReadLine();

        }
    }
}
