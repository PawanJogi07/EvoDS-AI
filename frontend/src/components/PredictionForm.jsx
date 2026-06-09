import { useEffect, useState } from "react";
import API from "../services/api";

function PredictionForm() {

const [features, setFeatures] = useState([]);

const [form, setForm] = useState({});

const [prediction, setPrediction] = useState("");

const [loading, setLoading] = useState(false);

useEffect(() => {


fetchModelInfo();


}, []);

const fetchModelInfo = async () => {


try {

  const res = await API.get(
    "/model-info"
  );

  setFeatures(
    res.data.features || []
  );

  const initialForm = {};

  res.data.features.forEach(
    (feature) => {

      initialForm[
        feature
      ] = "";

    }
  );

  setForm(
    initialForm
  );

} catch (error) {

  console.error(
    error
  );

}


};

const handleChange = (e) => {


setForm({
  ...form,
  [e.target.name]:
  e.target.value
});


};

const handlePredict = async () => {


try {

  setLoading(true);
  setPrediction(""); // Clear previous prediction

  const payload = {};

  Object.keys(form).forEach(
    (key) => {

      const value =
        form[key];

      if (
        value !== "" &&
        !isNaN(value)
      ) {

        payload[key] =
          Number(value);

      } else {

        payload[key] =
          value;

      }

    }
  );

  const res =
    await API.post(
      "/predict",
      payload
    );

  setPrediction(
    res.data.prediction
  );

} catch (error) {

  console.error(
    error
  );

  setPrediction("error");

} finally {

  setLoading(false);

}


};

return (


<div>

  <h2>
    Prediction
  </h2>

  <div className="grid">

    {features.map(
      (feature) => (

        <input
          key={feature}
          name={feature}
          placeholder={feature}
          value={
            form[
              feature
            ] || ""
          }
          onChange={
            handleChange
          }
        />

      )
    )}

  </div>

  <br />

  <button
    onClick={
      handlePredict
    }
    disabled={loading}
    style={{
      opacity: loading ? 0.6 : 1,
      cursor: loading ? "not-allowed" : "pointer"
    }}
  >

    {loading
      ? "Predicting..."
      : "Predict"}

  </button>

  {prediction && prediction !== "error" && (

    <div
      className="prediction-card"
      style={{
        marginTop: "20px",
        padding: "15px",
        backgroundColor: "#d4edda",
        border: "1px solid #c3e6cb",
        borderRadius: "5px"
      }}
    >

      <h3>
        ✅ Prediction Result
      </h3>

      <h2 style={{ color: "#155724" }}>
        {prediction}
      </h2>

    </div>

  )}

  {prediction === "error" && (

    <div
      style={{
        marginTop: "20px",
        padding: "15px",
        backgroundColor: "#f8d7da",
        border: "1px solid #f5c6cb",
        borderRadius: "5px"
      }}
    >

      <h3 style={{ color: "#721c24" }}>
        ❌ Prediction Failed
      </h3>

      <p style={{ color: "#721c24" }}>
        Unable to make prediction. Please check your input values.
      </p>

    </div>

  )}

</div>


);

}

export default PredictionForm;
