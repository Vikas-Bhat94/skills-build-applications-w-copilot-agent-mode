import octofitLogo from '../public/octofitapp-small.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <nav>
        <img src={octofitLogo} className="octofit-logo" alt="Octofit Logo" />
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">Activities</a></li>
          <li><a href="#">Teams</a></li>
          <li><a href="#">Leaderboard</a></li>
          <li><a href="#">Profile</a></li>
        </ul>
      </nav>
      <header className="App-header">
        <h1>Octofit Tracker</h1>
        <p>
          Welcome to your fitness journey! Track activities, join teams, and compete on the leaderboard.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
