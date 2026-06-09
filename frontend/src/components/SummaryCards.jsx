function SummaryCards({ report }) {

  return (

    <div
      style={{
        display: "flex",
        gap: "20px",
        marginTop: "20px"
      }}
    >

      <div className="card">
        <h3>Rows</h3>
        <h1>{report.rows}</h1>
      </div>

      <div className="card">
        <h3>Columns</h3>
        <h1>{report.columns}</h1>
      </div>

      <div className="card">
        <h3>Revenue</h3>
        <h1>
          {report.total_revenue
            ? `₹${report.total_revenue}`
            : "N/A"}
        </h1>
      </div>

    </div>

  );

}

export default SummaryCards;