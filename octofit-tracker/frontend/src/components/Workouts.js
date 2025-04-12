import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    const fetchWorkouts = async () => {
      const response = await fetch(`https://automatic-halibut-g6g5x667pqwhv6r6-8000.app.github.dev/api/workouts`);
      const data = await response.json();
      setWorkouts(data);
    };

    fetchWorkouts();
  }, []);

  return (
    <div className="card">
      <div className="card-body">
        <h1 className="card-title">Workouts</h1>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map(workout => (
              <tr key={workout.id}>
                <td>{workout.id}</td>
                <td>{workout.name}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Workouts;