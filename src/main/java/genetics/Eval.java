package genetics;

import java.util.Arrays;
import java.util.List;

import io.jenetics.Chromosome;
import io.jenetics.DoubleChromosome;
import io.jenetics.Genotype;
import io.jenetics.IntegerChromosome;

@SuppressWarnings({"rawtypes", "unchecked"})
public class Eval {
    public static final Genotype ENCODING = Genotype.of(
        DoubleChromosome.of(0, 100, 5),
        (Chromosome)IntegerChromosome.of(0, 3, 4)
    );
    
    public static double fitness(final Genotype gt) {
        DoubleChromosome numbers = (DoubleChromosome)gt.get(0);
        IntegerChromosome operations = (IntegerChromosome)gt.get(1);

        double total = numbers.get(0).doubleValue();
        for (var i = 0; i < operations.length(); i++) {
            total = fitness_eval(total, operations.get(i).intValue(), numbers.get(i+1).doubleValue());
        }
        
        return - Math.abs(3.14159 - total);
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
