import * as React from 'react';
import { useState } from 'react';
import logo from './logo.svg';
import './App.css';

const App = () => {
  const [gameId, setGameId] = useState(0);

  const gameStart = (event) => {
    event.preventDefault();

    fetch('/api/start')
      .then((res) => res.json())
      .then((data) => {
        setGameId(data.gameId);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <p>The game ID is {gameId}</p>
        <button type="button" onClick={gameStart}>
          Start Game!
        </button>
      </header>
    </div>
  );
};

export default App;
