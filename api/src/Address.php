<?php
/**
 * @Entity @Table(name="addresses")
 **/
class Address
{
    /** @Id @Column(type="integer") @GeneratedValue **/
    protected $id;

    /** @Column(type="text") **/
    protected $address;

    /**
     * @ManyToOne(targetEntity="Location")
     * @JoinColumn(name="location_id", referencedColumnName="id")
     */
    protected $location;

    public function getId()
    {
        return $this->id;
    }

    public function setAddress( $address )
    {
        $this->address = $address;
    }

    public function getAddress()
    {
        return $this->address;
    }

    public function setLocation( $location )
    {
        return $this->location = $location;
    }

    public function getLocation()
    {
        return $this->location;
    }
}
