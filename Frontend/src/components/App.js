
import React from "react"

import Header from "./common/Header"
import Footer from "./common/Footer"

export default class App extends React.Component {

  render() {

    return(
      <main>
        <Header></Header>

        <div className="container">
          <h1 className="text-center">Main</h1>
        </div>

        <Footer></Footer>
      </main>
    )
  }
}
