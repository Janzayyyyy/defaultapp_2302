{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import request, render_template\n",
    "\n",
    "@app.route(\"/\", methods=[\"GET\", \"POST\"])\n",
    "def index():\n",
    "    if request.method==\"POST\":\n",
    "        Income = request.form.get(\"Income\")\n",
    "        Age = request.form.get(\"Age\")\n",
    "        Loan = request.form.get(\"Loan\")\n",
    "        print(Income, Age, Loan)\n",
    "        Income = (float(Income) - 45133.788162)/ 14426.484876\n",
    "        Age = (float(Age) - 34.860629)/ 12.654700\n",
    "        Loan = (float(Loan) - 5591.682849)/ 3174.972365\n",
    "        model = joblib.load(\"default\")\n",
    "        pred = model.predict([[float(Income), float(Age), float(Loan)]])\n",
    "        if pred == 0:\n",
    "            score = \"No default\"\n",
    "        elif pred == 1:\n",
    "            score = \"Default\"\n",
    "        s = \"The predicted default score is \" + str(pred) + f\" ({score})\"\n",
    "        return(render_template(\"index.html\", result=s))\n",
    "    else:\n",
    "        return(render_template(\"index.html\", result=\"2\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [26/Feb/2022 17:30:57] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [26/Feb/2022 17:31:03] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10000 30 4000\n"
     ]
    }
   ],
   "source": [
    "app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
