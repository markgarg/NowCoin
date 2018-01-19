
  var componentStyle = {
    height: "500px",
  }

  var host_url = window.location.href

    class Component extends React.Component {
      constructor(props){
        super(props)
        this.state = {
          status: "Null",
          task_id: null,
          engaged: false
        }
        this.startJob = this.startJob.bind(this)
        this.updateStatus = this.updateStatus.bind(this)
      }

      updateStatus(task_id){
        var this_ = this
        this.setState({status: "Changed"})

        $.get(host_url+"status/"+task_id, function(data, status){
          // console.log("Status: ", data)
          if (data == "SUCCESS") {
            this_.setState({
              status : "It's a success",
              engaged: false
            })
          } else if (data == "PENDING") {
            this_.setState({status : "Pending..."})
            setTimeout(function() {
              this_.updateStatus(task_id);
            }, 2000)
          } else {
            this_.setState({status : "There's been an error"})
          }
        })
      }

      startJob(e){
        var this_ = this
        $.post(host_url+"task", function(data, status){
          console.log("task_id: ", data)
          this_.setState({engaged:true})
          this_.updateStatus(data)
        })
      }

      render(){

        var enabledButton = <button className="waves-effect waves-light btn-large" onClick={(e) => this.startJob(e)}>Click</button>
        var disableButton = <button className="btn-large disabled" onClick={(e) => this.startJob(e)}>Click</button>
        var button = (this.state.engaged) ? disableButton : enabledButton ;
          return(
            <div className="col s6">
              <div className="card-panel">
                <h3>{this.props.name}</h3>
                <br/><br/>
                <h5>Status: {this.state.status}</h5>
                <br/><br/>
                {button}
              </div>
            </div>)
      }
    }

    ReactDOM.render(
      <div className="row">
        <Component name="Component 1"/>
        <Component name="Component 2"/>
      </div>,
      document.getElementById('component')
    )
