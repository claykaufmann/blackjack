import * as React from 'react';
import { useState } from 'react';
import logo from './logo.svg';
import './App.css';

const App = () => {
  const [gameId, setGameId] = useState(0);

  const [gameHasStarted, setGameStart] = useState(false);

  const [returnData, setReturnData] = useState('');

  const sendData = (event) => {
    event.preventDefault();

    fetch(`api/test_game/${gameId}`, {
      method: 'POST',
      body: {
        name: 'Hi!',
        action: 'hit',
      },
    })
      .then((res) => res.json())
      .then((data) => {
        setReturnData(data.game_id);
      });
  };

  const gameStart = (event) => {
    // check if the game has already started
    if (gameHasStarted) {
      return;
    }

    event.preventDefault();

    fetch('/api/start')
      .then((res) => res.json())
      .then((data) => {
        setGameId(data.gameId);
      });

    setGameStart(true);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>The game ID is {gameId}</p>
        {gameHasStarted ? (
          <div>
            <button type="button" onClick={sendData}>
              Send Data!
            </button>
            <p>{returnData}</p>
          </div>
        ) : (
          <button type="button" onClick={gameStart}>
            Start Game!
          </button>
        )}
      </header>
    </div>
  );
};

export default App;
