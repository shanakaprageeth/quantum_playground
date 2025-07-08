// import ms quantum libs
import Microsoft.Quantum.Measurement;
import Microsoft.Quantum.Intrinsic;
// import standard libs
import Std.Intrinsic.*;

// Use entrypoint as main or just use main
@EntryPoint()
operation HelloWorld() : Result[] {
    let nBits = 5;
    use register = Qubit[nBits];
    for qubit in register {
        H(qubit);
    }
    Message($"Hello {nBits} qubits world!");
    let results = MeasureEachZ(register);
    ResetAll(register);
    Message($"Hello world! Random {nBits} qbit H Gate output");
    return results;
}

// commented out here as we use @entrypoint
//operation Main() : Result {
//   
//}