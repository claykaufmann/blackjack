import * as React from 'react';
import { useState } from 'react';
import Player from './Player';
import logo from './logo.svg';
import './App.css';

const App = () => {
  const [gameId, setGameId] = useState(0);

  const [gameStatus, setGameStatus] = useState(false);

  const [players, setPlayers] = useState(0);

  const [playerCards, setPlayerCards] = useState(0);

  const [gameHasStarted, setGameStart] = useState(false);

  // TODO: remove this when further in development
  const [returnData, setReturnData] = useState('');

  const sendData = (event) => {
    event.preventDefault();

    fetch(`api/test_game/${gameId}`, {
      method: 'POST',
      type: 'JSON',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        test: 'Hi!',
        action: 'hit',
      }),
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
        setGameId(data.game_id);
        // setPlayerCards(data.player.cards);
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
            <Player value={players.dealer.value} cards={cards.dealer} />
            <Player value={players.player.value} cards={cards.player} />
            <button type="button" onClick={sendData}>
              Send Data!
            </button>
            <p>{returnData}</p>
            {/* <p>{playerCards}</p> */}
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
