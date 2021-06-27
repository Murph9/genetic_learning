package genetics;

import java.util.concurrent.CompletableFuture;

import io.jenetics.Chromosome;
import io.jenetics.DoubleChromosome;
import io.jenetics.Genotype;
import io.jenetics.IntegerChromosome;

@SuppressWarnings({"rawtypes", "unchecked"})
public class Eval {
    private static final double TARGET = Math.PI;
    private static final int ENCODING_LENGTH = 3;
    public static final Genotype ENCODING = Genotype.of(
        DoubleChromosome.of(0, 100, ENCODING_LENGTH + 1),
        (Chromosome)IntegerChromosome.of(0, 3, ENCODING_LENGTH)
    );
    
    public static CompletableFuture<Double> asyncFitness(final Genotype gt) {
        return CompletableFuture.completedFuture(fitness(gt));
    }

    private static double fitness(final Genotype gt) {
        DoubleChromosome numbers = (DoubleChromosome)gt.get(0);
        IntegerChromosome operations = (IntegerChromosome)gt.get(1);

        double total = numbers.get(0).doubleValue();
        for (var i = 0; i < operations.length(); i++) {
            total = fitness_eval(total, operations.get(i).intValue(), numbers.get(i+1).doubleValue());
        }
        
        return - Math.abs(TARGET - total);
    }

    private static double fitness_eval(double existing, int value, double newValue) {
        try {
            switch(value) {
                case 0:
                    return existing + newValue;
                case 1:
                    return existing - newValue;
                case 2:
                    return existing * newValue;
                case 3:
                    return existing / newValue;
            }
        } catch (Exception e) {} // evolution hears no exceptions

        return Double.NaN;
    }
}
