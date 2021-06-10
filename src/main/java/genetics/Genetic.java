package genetics;

import io.jenetics.Phenotype;
import io.jenetics.engine.Engine;
import io.jenetics.engine.EvolutionResult;

public class Genetic {
    public static void main(String[] args) {

        // Create the execution environment.
        final Engine engine = Engine
            .builder(Eval::fitness, Eval.ENCODING)
            .build();
    
        // Start the execution (evolution) and collect the result.
        final Phenotype result = (Phenotype)engine.stream()
            .limit(100)
            .collect(EvolutionResult.toBestPhenotype());
    
        System.out.println("Hello World:\n" + result);
    }
}