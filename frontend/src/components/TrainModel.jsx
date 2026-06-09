import { useState } from "react";
import API from "../services/api";

function TrainModel() {

  const [target, setTarget] = useState("");
  const [result, setResult] = useState(null);

  const handleTrain = async () => {

    try {

      const res = await API.post(
        `/train-model?target=${target}`
      );

      setResult(res.data);
      setTimeout(() => {
  window.location.reload();
}, 1000);

    } catch (error) {

      console.error(error);

    }
  };

  return (
    <div>

      <h2>Train Model</h2>

      <input
        placeholder="Target Column"
        value={target}
        onChange={(e) =>
          setTarget(e.target.value)
        }
      />

      <button
        onClick={handleTrain}
        style={{ marginLeft: "10px" }}
      >
        Train
      </button>

      {result && (

        <div
          className="card"
          style={{ marginTop: "20px" }}
        >

          <h3>Dataset</h3>
          <p>{result.dataset}</p>

          <h3>Target</h3>
          <p>{result.target}</p>

          <h3>Accuracy</h3>
          <p>{result.accuracy}%</p>

          {result.best_model && (
            <>
              <h3>Best Model</h3>
              <p>{result.best_model}</p>
            </>
          )}

        </div>

      )}

      {result?.leaderboard && (

        <>
          <h2
            style={{
              marginTop: "20px"
            }}
          >
            Model Leaderboard
          </h2>

          <div className="grid">

            {Object.entries(
              result.leaderboard
            ).map(
              ([model, score]) => (

                <div
                  className="card"
                  key={model}
                >
                  <h3>{model}</h3>
                  <h2>{score}%</h2>
                </div>

              )
            )}

          </div>

        </>

      )}

    </div>
  );
}

export default TrainModel;