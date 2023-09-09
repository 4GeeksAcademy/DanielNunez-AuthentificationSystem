import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<>
			<div className="text-center mt-5">
				<p>
					This boilerplate comes with lots of documentation:{" "}
					<a href="https://start.4geeksacademy.com/starters/react-flask">
						Read documentation
					</a>
				</p>
			</div>
			<div className="container">
				<form className="col-sm-12 col-md-8 col-lg-10">
					<div className="mb-3">
						<label className="form-label">Email address</label>
						<input type="email" className="form-control" name="email"/>
						<div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
					</div>
					<div className="mb-3">
						<label className="form-label">Password</label>
						<input type="password" className="form-control" name="password" />
					</div>
					<div className="mb-3 form-check">
						<input type="checkbox" className="form-check-input" name="checkBox" />
						<label className="form-check-label">Check me out</label>
					</div>
					<button type="submit" className="btn btn-primary">Submit</button>
				</form>
			</div>
		</>

	);
};