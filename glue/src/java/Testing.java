/* simple Testing class */

import org.bitcoinj.core.*;
import org.bitcoinj.script.*;
import org.bitcoinj.core.Transaction.SigHash;
import org.bitcoinj.crypto.TransactionSignature;
import org.bitcoinj.params.MainNetParams;
import org.bitcoinj.params.TestNet3Params;
import org.bitcoinj.script.Script.VerifyFlag;

import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.nio.charset.Charset;
import java.util.*;

import static org.bitcoinj.core.Utils.HEX;
import static org.bitcoinj.script.ScriptOpCodes.OP_0;
import static org.bitcoinj.script.ScriptOpCodes.OP_INVALIDOPCODE;

public class Testing {

  static final String sigProg = "47304402202b4da291cc39faf8433911988f9f49fc5c995812ca2f94db61468839c228c3e90220628bff3ff32ec95825092fa051cba28558a981fcf59ce184b14f2e215e69106701410414b38f4be3bb9fa0f4f32b74af07152b2f2f630bc02122a491137b6c523e46f18a0d5034418966f93dfc37cc3739ef7b2007213a302b7fba161557f4ad644a1c";

  static final String pubkeyProg = "76a91433e81a941e64cda12c6a299ed322ddbdd03f8d0e88ac";

  static final NetworkParameters params = MainNetParams.get();

  public static void addr(byte[] sigbytes){

    Script script = new Script(sigbytes);
    // Test we can extract the from address.
    byte[] hash160 = Utils.sha256hash160(script.getPubKey());
    Address a = new Address(params, hash160);

    System.out.println("addr: " + a);
    //assertEquals("mkFQohBpy2HDXrCwyMrYL5RtfrmeiuuPY2", a.toString());
  }

  //address example
  public static void addr(){

    byte[] sigProgBytes = HEX.decode(sigProg);
    Script script = new Script(sigProgBytes);
    // Test we can extract the from address.
    byte[] hash160 = Utils.sha256hash160(script.getPubKey());
    Address a = new Address(params, hash160);

    System.out.println("addr: " + a);
    //assertEquals("mkFQohBpy2HDXrCwyMrYL5RtfrmeiuuPY2", a.toString());
  }

  public static int vier(){
    return 4;
  }

}
