(ns glue.example
  (:require [midje.sweet :refer :all]
            [cljpy.core :as base]
            [buddy.core.hash :as hash]
            [buddy.core.codecs :refer :all])
  (:import Testing)
  (:import Base58)
  (:import (org.bitcoinj.script.ScriptOpCodes))
  (:import (org.bitcoinj.script.ScriptBuilder))
  (:import (org.bitcoinj.core.Utils.HEX))
  (:import (org.bitcoinj.script.Script)))

;(defmacro op [x & args]
;  `(. java.lang.Math ~x ~@args))

;script macro op code
(defmacro sop [x & args]
 `(. org.bitcoinj.script.ScriptOpCodes ~x ~@args))

;https://blockchain.info/tx/caa6b45bb52258a6acf8deb440442f2d4393bb50a62d53ed5fc57e78c1ec4905?format=hex

(defmacro with-test-interp [& body]
 `(base/with-interpreter
    {:libpaths ["src/py/"]}
    ~@body))

(def pubkeyProg "76a91433e81a941e64cda12c6a299ed322ddbdd03f8d0e88ac")

;return new ScriptBuilder()
;                .op(OP_DUP)
;                .op(OP_HASH160)
;                .data(to.getHash160())
;                .op(OP_EQUALVERIFY)
;                .op(OP_CHECKSIG)
;                .build();

(defn demo-interop
  "demontsrate interop"
  []
  (println "main")
  (with-test-interp
    (base/py-import-lib example)
    (base/import-fn example hello)
    (base/import-fn example calc)
    (println (hello "world"))
    (println (calc 2)))

  (Testing/addr)
  (println (-> (hash/sha256 "Lykkex1")
    (bytes->hex)))

  ;(println (sop OP_0))
  ;(println (org.bitcoinj.script.ScriptOpCodes/OP_0))

  (println (sop OP_0))

  (println (hex->bytes pubkeyProg))

  (println (new org.bitcoinj.script.Script (hex->bytes pubkeyProg)))

  ;byte[] pubkeyBytes = HEX.decode(pubkeyProg);
  ;      Script pubkey = new Script(pubkeyBytes);

  (println "main end"))

(defn -main []
  (demo-interop)
  (println (Base58/encode (.getBytes "test")))
  (println "--main end--"))
