import { useState, useEffect } from "react";
import { Container, Row, Col } from "react-bootstrap";
import headerImg from "../assets/img/Chat bot-pana.svg";
import { ArrowRightCircle } from 'react-bootstrap-icons';
import 'animate.css';
import TrackVisibility from 'react-on-screen';

export const Banner = () => {
  const [loopNum, setLoopNum] = useState(0);
  const [isDeleting, setIsDeleting] = useState(false);
  const [text, setText] = useState('');
  const [delta, setDelta] = useState(300 - Math.random() * 100);
  const [index, setIndex] = useState(1);
  const toRotate = [ "Natural", "Language", "Processing" ];
  const period = 2000;

  useEffect(() => {
    let ticker = setInterval(() => {
      tick();
    }, delta);

    return () => { clearInterval(ticker) };
  }, [text])

  const tick = () => {
    let i = loopNum % toRotate.length;
    let fullText = toRotate[i];
    let updatedText = isDeleting ? fullText.substring(0, text.length - 1) : fullText.substring(0, text.length + 1);

    setText(updatedText);

    if (isDeleting) {
      setDelta(prevDelta => prevDelta / 2);
    }

    if (!isDeleting && updatedText === fullText) {
      setIsDeleting(true);
      setIndex(prevIndex => prevIndex - 1);
      setDelta(period);
    } else if (isDeleting && updatedText === '') {
      setIsDeleting(false);
      setLoopNum(loopNum + 1);
      setIndex(1);
      setDelta(500);
    } else {
      setIndex(prevIndex => prevIndex + 1);
    }
  }

  return (
    <section className="banner" id="home">
      <Container>
        <Row className="aligh-items-center">
          <Col xs={12} md={6} xl={7}>
            <TrackVisibility>
              {({ isVisible }) =>
              <div className={isVisible ? "animate__animated animate__fadeIn" : ""}>
                <span className="tagline">UPES - OPEN presents</span>
                <h1>{`Analysis of Products using... `} 
                    <span className="txt-rotate" dataPeriod="1000" data-rotate='["Natural", "Language", "Processing"]'>
                        <span className="wrap">{text}</span>
                    </span>
                </h1>
                <p>
                  A platform(website) where you can enter a product's description to check if similar 
                  products exist in the market already. If they do, then you can get all the information 
                  about the products, the similarities between the products and how it was accepted by 
                  the consumers. If the consumers had mixed reviews, then you can filter out the 
                  positive/negative reviews according to your need to understand the consumer market of 
                  that product. Different NLP methods can be used for getting deeper understanding of Consumers. 
                  This can be used to determine if one should go forward into making that product, or what are 
                  the specific thing that has been done by its competitors that brought them a great success 
                  as compared to the ones who failed. 
                </p>
                <button onClick={() => console.log('connect')}>Check it out! <ArrowRightCircle size={29} /></button>
              </div>}
            </TrackVisibility>
          </Col>
          <Col xs={12} md={6} xl={5}>
            <TrackVisibility>
              {({ isVisible }) =>
                <div className={isVisible ? "animate__animated animate__zoomIn" : ""}>
                  <img src={headerImg} alt="Header Img"/>
                </div>}
            </TrackVisibility>
          </Col>
        </Row>
      </Container>
    </section>
  )
}