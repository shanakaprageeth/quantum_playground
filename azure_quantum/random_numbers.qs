import Std.Diagnostics.DumpMachine;
// import ms quantum libs
import Microsoft.Quantum.Measurement;
import Microsoft.Quantum.Intrinsic;
import Microsoft.Quantum.Convert.*;
import Microsoft.Quantum.Math.*;
import Microsoft.Quantum.Diagnostics.*;

// import standard libs
import Std.Intrinsic.*;


operation RandomQbitMeasurement(nBits: Int) : Result[] {
    use register = Qubit[nBits];
    for qubit in register {
        H(qubit);
    }
    DumpMachine();
    let results = MeasureEachZ(register);
    DumpMachine();
    ResetAll(register);
    Message($"Random {nBits} qbit H Gate output");
    return results;
}

operation GenerateRandomNumberInLength(max : Int) : Int {
    mutable bits = [];
    let sysBits = 5;
    let nBits = BitSizeI(max);

    mutable collected = 0;
    while (collected < nBits) {
        let chunkSize = MinI(sysBits, nBits - collected);
        let chunk = RandomQbitMeasurement(chunkSize);
        set bits += chunk;
        set collected += chunkSize;
    }
    let sample = ResultArrayAsInt(bits[0..nBits-1]);
    
    // Return random number if it is within the requested range.
    // Generate it again if it is outside the range.
    return sample > max ? GenerateRandomNumberInLength(max) | sample;
}

operation Main() : Int{
   let len = 100;
    Message($"Sampling a random number between 0 and {len} ");
    return GenerateRandomNumberInLength(len);
}