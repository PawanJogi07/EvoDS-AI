function Leaderboard({ leaderboard }) {

  if (!leaderboard) return null;

  return (
    <div className="grid">
      {Object.entries(leaderboard).map(
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
  );
}

export default Leaderboard;