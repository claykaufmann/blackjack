import * as React from 'react';

const Card = (props) => {
  const data = props;
  const { value, suit, visibility } = data;

  let card = <></>;
  /* switch case for suits */
  // let cSuit = '';

  // switch(suit) {
  //   case 'Hearts':
  //     cSuit = <>&hearts</>;
  //     break;

  //   case 'Diamonds':
  //     cSuit = <>&diams</>;
  //     break;

  //   case 'Spades':
  //     cSuit = <>&spades</>;
  //     break;

  //   case 'Clubs':
  //     cSuit = <>&clubs</>;
  //     break;

  //   default:
  //     break;
  // }

  if (visibility === false) {
    card = (
      <>
        <p className="Card-backside" />
      </>
    );
  } else {
    card = (
      <>
        <p className="Card-front">
          {value} of {suit}
        </p>
      </>
    );
  }

  return <div className="Card">{card}</div>;
};

export default Card;
