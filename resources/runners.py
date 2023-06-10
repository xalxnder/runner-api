from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import RunnersSchema
from models import RunnersModel
from db import db
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("runners", __name__, description="Operations on runners.")


@blp.route("/runners/<string:runner_id>")
class RunnersByID(MethodView):
    """
    blp.response = what we're sending from the API to the client.
    Since id is set to dump in our schema, tihs is what gets sent back to us
    in the response.
    """

    @blp.response(200, RunnersSchema)
    def get(self, runner_id):
        """ query.get_or_404 -
        Like get() but aborts with a 404 Not Found error instead of returning None.
        """
        runner = RunnersModel.query.get_or_404(runner_id)
        return runner

    def delete(self, runner_id):
        runner = RunnersModel.query.get_or_404(runner_id)
        db.session.delete(runner)
        db.session.commit()
        return {"message": "Runner removed"}


@blp.route("/runners")
class Runners(MethodView):
    @blp.response(200, RunnersSchema(many=True))
    def get(self):
        return RunnersModel.query.all()

    @blp.arguments(RunnersSchema)
    @blp.response(201, RunnersSchema)
    # runner_data is the json data we're passing
    def post(self, runner_data):
        runner = RunnersModel(**runner_data)
        try:
            # This adds, but does not save it.
            db.session.add(runner)
            # Committing actually saves it
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="uh oh")
            pass
        return runner
