import { Container, Row, Col } from "react-bootstrap";
import { MailchimpForm } from "./MailchimpForm";
import navIcon1 from "../assets/img/nav-icon1.svg";
import navIcon3 from "../assets/img/nav-icon3.svg";
import navIcon4 from "../assets/img/github.svg";

export const Footer = () => {
  return (
    <footer className="footer" id="footer">
      <Container>
        <Row className="align-items-center">
          <MailchimpForm />
          <Col size={12} sm={6}>
          <a href="https://upes-open.org/" target="_blank"><h1>UPES-OPEN</h1></a>
          </Col>
          <Col size={12} sm={6} className="text-center text-sm-end">
            <div className="social-icon">
              <a href="https://www.linkedin.com/company/open-community/" target="_blank"><img src={navIcon1} alt="linkedin" /></a>
              <a href="https://github.com/upes-open" target="_blank"><img src={navIcon4} alt="github" /></a>
              <a href="https://www.instagram.com/upesopen_/" target="_blank"><img src={navIcon3} alt="" /></a>
            </div>
            <p>Created by UPES-OPEN Team</p>
          </Col>
        </Row>
      </Container>
    </footer>
  )
}