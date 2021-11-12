import * as React from 'react';
import Card from './Card';

const Player = (props) => {
  const data = props;
  const { cards } = data;
  const { value } = data;
  const { playerName } = data;

  return (
    <>
      <p>
        {playerName} hand value is {value}
      </p>
      {cards.map((card) => (
        <Card value={card[0]} suit={card[1]} />
      ))}
    </>
  );
};

export default Player;
