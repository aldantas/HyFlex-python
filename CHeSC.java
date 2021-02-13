import AbstractClasses.HyperHeuristic;
import AbstractClasses.ProblemDomain;


public class CHeSC extends HyperHeuristic {

    private String name = "CHeSC HyperHeuristic";

	public CHeSC(long seed, long timeLimit, ProblemDomain problem){
		super(seed);
        setTimeLimit(timeLimit);
        loadProblemDomain(problem);
	}

    public void startTimer() {
        //starts the timer, and then calls the solve() method
        run();
    }

    //empty method to be called by run()
    //the algorithm must be implemented on the python side
    public void solve(ProblemDomain problem) {}

    //exposes the protected hasTimeExpired method
    public boolean hasRuntimeExpired() {
        return hasTimeExpired();
    }

    public void setName(String name) {
        this.name = name;
    }

	public String toString() {
		return name;
	}
}
