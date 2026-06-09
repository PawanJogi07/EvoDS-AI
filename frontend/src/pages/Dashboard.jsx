import { useEffect, useState } from "react";
import API from "../services/api";
import SummaryCards from "../components/SummaryCards";
import PredictionForm from "../components/PredictionForm";
import UploadSection from "../components/UploadSection";
import TrainModel from "../components/TrainModel";

function Dashboard() {

  const [report, setReport] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchEDA = async () => {

    try {

      setLoading(true);
      setError(null);

      const res = await API.get("/eda-report");

      setReport(res.data);
      setError(null);

    } catch (error) {

      console.error(error);

      setError(
        error.response?.data?.detail ||
        "Failed to load EDA report"
      );
      setReport(null);

    } finally {

      setLoading(false);

    }

  };

  useEffect(() => {

    fetchEDA();

  }, []);

  const handleUploadSuccess = () => {
    fetchEDA();
  };

  const handleRetry = () => {
    fetchEDA();
  };

  if (loading && !report) {
    return (
      <div style={{ padding: "30px" }}>
        <h1>EvoDS AI</h1>

        <p
          style={{
            color: "#94a3b8",
            fontSize: "18px",
            marginBottom: "25px"
          }}
        >
          Autonomous Data Science Platform 🚀
        </p>

        <UploadSection
          onUploadSuccess={handleUploadSuccess}
        />
        <h2>Loading...</h2>
      </div>
    );
  }

  if (error && !report) {

    return (

  <div style={{ padding: "30px" }}>

    <h1>EvoDS AI</h1>

    <p
      style={{
        color: "#94a3b8",
        fontSize: "18px",
        marginBottom: "25px"
      }}
    >
      Autonomous Data Science Platform 🚀
    </p>

    <UploadSection
      onUploadSuccess={fetchEDA}
    />

        <h3 style={{ color: "red" }}>
          ⚠️ {error}
        </h3>

        <button 
          onClick={handleRetry}
          style={{
            padding: "10px 20px",
            marginTop: "10px",
            cursor: "pointer",
            backgroundColor: "#007bff",
            color: "white",
            border: "none",
            borderRadius: "5px"
          }}
        >
          Retry
        </button>

      </div>

    );

  }

  return (

    <div style={{ padding: "30px" }}>

      <h1>EvoDS AI</h1>

      <p
        style={{
          color: "#94a3b8",
          fontSize: "18px",
          marginBottom: "25px"
        }}
      >
        Autonomous Data Science Platform 🚀
      </p>

      <UploadSection
        onUploadSuccess={handleUploadSuccess}
      />

      {loading && (
        <div style={{ color: "#666", fontStyle: "italic", margin: "10px 0" }}>
          Refreshing data...
        </div>
      )}

      <hr />

      <h2>Dataset Summary</h2>

      <p>
        <strong>Dataset:</strong>{" "}
        {report.filename}
      </p>

      <SummaryCards
        report={report}
      />

      <hr />

      <h2>Dataset Columns</h2>

      <div className="grid">

        {report.column_names?.map(
          (col) => (

            <div
              className="card"
              key={col}
            >
              <h3>{col}</h3>
            </div>

          )
        )}

      </div>

      <hr />

      <TrainModel />

      {report.charts && (

        <>

          <hr />

          <h2>Charts</h2>

          <div className="grid">

            {report.charts.map(
              (chart) => (

                <div
                  className="card"
                  key={chart}
                >

                  <img
  src={`http://127.0.0.1:8000/${chart}?t=${Date.now()}`}
  alt={chart}
  style={{
    width: "100%",
    borderRadius: "10px"
  }}
/>

                </div>

              )
            )}

          </div>

        </>

      )}

      <hr />

      <h2>Insights</h2>

      <ul>

        {report.insights?.map(
          (item, index) => (

            <li key={index}>
              {item}
            </li>

          )
        )}

      </ul>

      <hr />

      <PredictionForm
  key={report.filename}
/>

    </div>

  );

}

export default Dashboard;