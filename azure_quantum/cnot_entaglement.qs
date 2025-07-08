import Std.Diagnostics.DumpMachine;
// import ms quantum libs
import Microsoft.Quantum.Measurement;
import Microsoft.Quantum.Intrinsic;
import Microsoft.Quantum.Convert.*;
import Microsoft.Quantum.Math.*;
import Microsoft.Quantum.Diagnostics.*;


operation HPauliCNOT() : (Result, Result) {
    use (qControl, qTarget) = (Qubit(), Qubit());
    H(qControl);
    Z(qControl); // Apply the Pauli Z operation to the control qubit
    CNOT(qControl, qTarget);
    DumpMachine();
    let (m1, m2) = (M(qControl), M(qTarget));
    DumpMachine();
    Reset(qControl);
    Reset(qTarget);

    return (m1, m2);
}

operation HCNOT() : (Result, Result) {
    use (qControl, qTarget) = (Qubit(), Qubit());
    H(qControl);
    CNOT(qControl, qTarget);
    DumpMachine();
    let (m1, m2) = (M(qControl), M(qTarget));
    DumpMachine();
    Reset(qControl);
    Reset(qTarget);
    return (m1, m2);
}

operation Main() : (Result, Result) {
    // return BellState
    return HCNOT();
    //return HPauliCNOT();
}
