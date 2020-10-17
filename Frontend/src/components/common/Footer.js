
import React from "react"


export default class Footer extends React.Component {

    render() {

        return (
            <footer className="bg-light text-center text-lg-left">
                <div className="container p-4">
                    <div className="row">
                        <div className="col-lg-6 col-md-12 mb-4 mb-md-0">
                            <h5 className="text-uppercase">About The Project</h5>
                            <p>
                                This web application project is created by 
                                <strong><a className="text-dark" href="https://github.com/endalk200">endalk</a></strong>
                                It is Twitter clone with latest Teck Stacks used. Some of which are:
                            </p>
                            <div className="row">
                                <div className="col-md-6">
                                    <ul>
                                        <li>Django</li>
                                        <li>Django Rest Framework</li>
                                        <li>Django Rest Knox</li>
                                        <li>React JS</li>
                                    </ul>
                                </div>
                                <div className="col-md-6">
                                    <ul>
                                        <li>MDB</li>
                                        <li>Github Actions</li>
                                        <li>Docker</li>
                                        <li>Kubernetes</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div className="col-lg-6 col-md-12 mb-4 mb-md-0">
                            <h5 className="text-uppercase">About The Author</h5>
                            <p>
                                My name is <strong><a className="text-dark" href="https://github.com/endalk200">Endalkachew Biruk</a></strong>. 
                                I am self tought full stack engineer with 2 Years of Experience. Programming Languages and scripting Languages
                                I am profficient in are Python, Javascript, Typescript and C# for programming language and Shell script, HTML5,
                                CSS3 / Sass / Less. I am also profficient in python libraries like Django, Django Rest Framework, Flask, Moviepy, 
                                Pillow, PyGame and others. Some of other Frameworks I use often are React, Material UI, MDB and other.
                            </p>
                        </div>
                    </div>
                </div>
                <div className="text-center p-3 footer_bg" >
                    © 2020 Copyright: created by <a className="text-dark" href="https://github.com/endalk200">endalk</a>
                </div>
            </footer>
        )
    }
}