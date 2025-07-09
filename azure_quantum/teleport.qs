import Std.Diagnostics.DumpMachine;
// import ms quantum libs
import Microsoft.Quantum.Measurement;
import Microsoft.Quantum.Intrinsic;
import Microsoft.Quantum.Convert.*;
import Microsoft.Quantum.Math.*;
import Microsoft.Quantum.Diagnostics.*;


// copying qbit to a remote end
operation sendQbit(message : Qubit, receiverq : Qubit) : Unit {
    use senderq = Qubit();

    // Create two entangled particles to keep one and send one to remote end
    // entangled pair
    H(senderq);
    CNOT(senderq, receiverq);

    // Encode the message into the entangled pair.
    CNOT(message, senderq);
    H(message);
    // Measure and send results to remote end with classical bits
    remoteEnd(receiverq, M(message), M(senderq));
    Reset(senderq);
}

// remote end will update the receiver qubit to clone to message qubit
operation remoteEnd(receiverq: Qubit, classicalMessage : Result, classicalSendq : Result) : Unit {
    use senderq = Qubit();
    if classicalMessage == One {
        Z(receiverq);
    }
    if classicalSendq == One {
        X(receiverq);
    }
}

// |0⟩ -> |+⟩.
operation SetToPlus(q : Qubit) : Unit is Adj + Ctl {
    H(q);
}

// |0⟩ -> |−⟩.
operation SetToMinus(q : Qubit) : Unit is Adj + Ctl {
    X(q);
    H(q);
}

@EntryPoint()
operation teleport() : Result[] {
    use (message, receiverq) = (Qubit(), Qubit());

    // Use the `Teleport` operation to send different quantum states.
    let stateInitializerBasisTuples = [
        ("|0〉", I, PauliZ),
        ("|1〉", X, PauliZ),
        ("|+〉", SetToPlus, PauliX),
        ("|-〉", SetToMinus, PauliX)
    ];

    mutable results = [];
    for (state, initializer, basis) in stateInitializerBasisTuples {
        // Initialize the message with all possible states for testing
        initializer(message);
        Message($"Teleporting state {state}");
        DumpMachine();

        // teleport the message to 
        sendQbit(message, receiverq);
        Message($"Received state {state}");
        DumpMachine();


        // measure the results and store them
        let result = Measure([basis], [receiverq]);
        set results += [result];
        ResetAll([message, receiverq]);
    }

    return results;
    
}
